# Emoji OnBoard keyboard layout

Tested on **Ubuntu 15.04 x64** but should work for any OS with **OnBoard** onscreen keyboard.

![screenshot](http://i.imgur.com/m880YhS.png)

## How to use

To display emoji you need to install font, which contain emoji symbols. Run command:

    sudo apt-get install ttf-ancient-fonts

will install «symbola» font, which contain most of Unicode 8.0 emoji.

Also you can install other emoji fonts like [Noto Emoji](https://github.com/googlei18n/noto-emoji) or [EmojiSymbols](http://emojisymbols.com/beforeuse.php).

Now copy all `layout` folder content to `~/.local/share/onboard/layouts` folder.

Then Go to `System Settings -> Accessibility` and in `Input` tab enable onscreen keyboard.

In layout select «emoji» in user's layouts.

I prefer open emoji keyboard by hotkey, so i disable auto show keyboard on input and autoclose on hardware keyboard press. It can be done on general OnBoard settings. And in `System Settings -> Keyboard` you can set keyboard shortcut which run `onboard` command. Play around with OnBoard settings to achieve most useful configuration.

## How to customize

Layout `.svg` template contain grid for 12x9 symbol buttons and for 16 panel switchers which allow display up to 12x9x16=1728 emoji. `.json` file contain obvious configuration for panels. `.onboard.template` contain common `.onboard` structure to generate layout. `.py` script generate new `.onboard` file in `layout` folder based on this config and onboard template.

**NOTE:** some emoji contain more than one symbol (including invisible characters) so by careful to operate with it.

How to modify `.svg` template you can read in your `/usr/share/onboard/docs/layouts.html`
