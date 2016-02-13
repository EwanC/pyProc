#!/usr/bin/env python3

class ProcBase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.handle = open(self.file_path, 'r')
        self.content = self.handle.read()

    def __exit__(self):
        self.handle.close()
