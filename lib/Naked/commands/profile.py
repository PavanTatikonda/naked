#!/usr/bin/env python
# encoding: utf-8

import os
from Naked.toolshed.system import file_exists, dir_exists, stderr

class Profiler:
    def __init__(self, dir_levels = 6):
        self.number_of_dir_levels = dir_levels # number of directory levels to bottom to top search

    def run(self):
        lib_found = False
        for i in range(self.number_of_dir_levels):
            if not self._is_lib_at_this_level():
                os.chdir(os.pardir)
            else:
                lib_found = True
                break
        if lib_found:
            os.chdir('lib') # chdir to the lib directory if it is found
            if file_exists('profiler.py'): # confirm that profiler.py exists
                os.system('python profiler.py') # run the profiler.py file
            else:
                stderr("Unable to locate a profiler.py file in your lib directory.", 1)
        else:
            stderr("Unable to locate your profiler.py file.  Please navigate to your project directory.", 1)

    def _is_lib_at_this_level(self):
        if dir_exists('lib'):
            return True
        else:
            return False
