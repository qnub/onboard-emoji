#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom


GRID_CONFIG = 'emoji-grid.json'
LAYOUT_FOLDER = 'layout'
LAYOUT_TEMPLATE = 'emoji.onboard.template'

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def prettify(elem):
    rough_string = ET.tostring(elem.getroot(), 'utf-8')
    reparsed = minidom.parseString(rough_string)

    return reparsed.toprettyxml(indent="  ")


def add_layer_key(keyboard, layer_id, title, label):
    key = ET.Element(
        'key_template',
        {
            'button': 'true',
            'id': 'layer{0}'.format(layer_id),
            'label': label,
            'tooltip': title,
        }
    )
    keyboard.insert(layer_id + 1, key)


def add_panel(parent, sys_keys, config):
    panel = ET.SubElement(
        parent,
        'panel',
        {
            'filename': config['layer_svg'],
            'layer': config['title'].replace(' ', '').lower(),
        }
    )

    row_num = 0

    for row in config['grid']:
        row_letter = chr(97 + row_num)
        key_num = 0

        for char in row:
            key_id = u'{0}{1}'.format(row_letter, key_num)
            ET.SubElement(
                panel,
                'key',
                {
                    'char': char,
                    'id': key_id,
                    'label': char,
                    'group': 'alphanumeric',
                }
            )

            key_num += 1

        row_num += 1

    panel.extend(sys_keys)


def generate_layout():
    config_filename = os.path.join(CURRENT_DIR, GRID_CONFIG)
    template_filename = os.path.join(CURRENT_DIR, LAYOUT_TEMPLATE)

    if not os.path.exists(config_filename):
        exit(u'Emoji grid config file "{0}" not found'.format(config_filename))

    if not os.path.exists(template_filename):
        exit(u'Emoji grid template file "{0}" not found'.format(template_filename))

    with open(config_filename, 'r') as config_file:
        config = json.load(config_file, 'utf-8')

    template = ET.parse(template_filename)

    folder = os.path.join(CURRENT_DIR, LAYOUT_FOLDER)
    filename = os.path.join(folder, u'.'.join(LAYOUT_TEMPLATE.split('.')[:-1]))

    if not os.path.exists(folder):
        os.makedirs(folder)

    keyboard = template.getroot()
    box = keyboard.find('box')
    panel_template = box.find('panel')
    box.remove(panel_template)
    sys_keys = panel_template.findall('key')
    layout_keys = []

    panel = ET.Element('panel')

    layer_id = 0

    for layer in config:
        add_layer_key(keyboard, layer_id, layer['title'], layer['label'])
        layer_id += 1
        add_panel(panel, sys_keys, layer)

    box.append(panel)

    with open(filename, 'w') as layout:
        layout.write(prettify(template).encode('utf-8'))

    print u'Layout "{0}" generated'.format(filename)


if __name__ == "__main__":
    generate_layout()
