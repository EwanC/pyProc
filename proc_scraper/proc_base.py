#!/usr/bin/env python3


class ProcBase:
    '''
    Virtual base class for all /proc/ subdirectory classes.

    Defines virtual methods for opening a file
    and reading data.

    Child classes will represent different folders/files in the
    /proc/ file system.
    '''

    underline_str = '=' * 80

    def __init__(self, file_path):
        '''
        Opens file and reads its contents.

        Keyword arguments:
        file_path -- path to file base class represents
        '''

        self.file_path = file_path
        try:
            self.handle = open(self.file_path, 'r')
            self.content = self.handle.read()
        except FileNotFoundError:
            self.content = []

    def __exit__(self):
        '''Close file handle when instance is destroyed'''
        if self.handle:
            self.handle.close()

    def dump(self):
        '''Print header identifying file parsed'''
        print()  # New line
        print(ProcBase.underline_str)
        print('Information in ', self.file_path)
        print(ProcBase.underline_str)
