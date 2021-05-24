import sys
import os

from pathlib import Path

from tool import *

class Directory:

    def __init__(self):
        if getattr(sys, 'frozen', False):
            self.root = os.path.dirname(sys.executable)
        elif __file__:
            self.root = os.path.dirname(__file__)
        self.tapes_name = "tapes"
        self.config_name = "config.txt"
        self.storage_name = "leafs.txt"
        self.read_target_directory()

    def read_target_directory(self):
        self.config = self.root + os.path.sep + self.config_name
        self.get_root_from_config()



        self.tapes = self.root + os.path.sep + self.tapes_name
        Path(self.tapes).mkdir(parents=True, exist_ok=True)
        self.tapes += os.path.sep

        self.storage = self.root + os.path.sep + self.storage_name
        if not Path(self.storage).is_file():
            save_file("", self.storage)

        print(self.config)
        print(self.root)
        print(self.tapes)
        print(self.storage)

    def get_root_from_config(self):
        if Path(self.config).is_file():
            paths = get_file_contents(self.config)

            for path in paths:
                if Path(path).is_dir():
                    self.root = path
                    return


