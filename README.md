# Quick File Switcher - Sublime plugin to toggle extensions

A Sublime Text plugin to quickly toggle between files in the same folder that share name but have different extensions.

I have only tested it on Sublime Text 3, let me know if you've tried it in version 4!

**Example:**

Open `Home.js`, press `alt+o` and `Home.css` opens. Press again and we're back to `Home.js`.

## Installation

Make sure you have Package Control installed: Press `Tools => Command Palette...`, type `Install Package Control`, press `enter`.

Then, open `Tools => Command Palette...` again, type `Install package` and press enter. Now, search for "QuickFileSwitcher" and press enter to install.

## How to

Press `alt+o` to switch between files. Files which have the same name but different extensions will be toggled between.

If it doesn't work for some reason, messages should be printed to the console, open it by going to `View => Show Console`.

## Custom keyboard shortcut

Not a fan of `alt+o`?

Open `Preferences -> Package Settings -> QuickFileSwitcher -> Key Bindings – User`, and add the following:

```
[
	{ "keys": ["ctrl+alt+delete"], "command": "quick_file_switcher"}
]
```

## How it works

It's very basic: Get current file name, list all files in its directory, open the first one that shares the same basename.

## License

This plugin is MIT Licensed.