from __future__ import print_function

from os import listdir
from os.path import splitext, split

import sublime
import sublime_plugin

class QuickFileSwitcherCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the current filename and split into its components
        path, name_and_ext = split(self.window.active_view().file_name())
        name, ext = splitext(name_and_ext)

        name_and_dot = "%s." % name

        # List files in the current directory
        for filename in listdir(path):
            # Skip the file we're already viewing
            if filename == name_and_ext:
                continue
            # We compare the filenames with the name and a trailing dot to mitigate against partial matches
            if filename.startswith(name_and_dot):
                self.window.open_file(filename)
                return

        print("QuickFileSwitcher: No files named %s with an extension other than %s were found" % (name, ext))
