#!/usr/bin/env python3

class ProcBase:
  
    underline_str = "=" * 80

    def __init__(self, file_path):
        self.file_path = file_path
        self.handle = open(self.file_path, 'r')
        self.content = self.handle.read()

    def __exit__(self):
        self.handle.close()

    def dump(self):
        print(ProcBase.underline_str)
        print("Information in ", self.file_path)
        print(ProcBase.underline_str)
