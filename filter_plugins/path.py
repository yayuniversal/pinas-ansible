#!/usr/bin/python
from pathlib import Path

class FilterModule(object):
    ''' Filter mappings for the pathlib.Path module '''

    def filters(self):
        return {
            'is_file': self.is_file,
            'is_dir': self.is_dir,
            'is_symlink': self.is_symlink
        }

    def is_file(self, path):
        return Path(path).is_file()
    
    def is_dir(self, path):
        return Path(path).is_dir()
    
    def is_symlink(self, path):
        return Path(path).is_symlink()
