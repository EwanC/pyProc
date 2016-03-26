#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcFileNR(ProcBase):
    '''Object represents the /proc/sys/fs/file-nr file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/sys/fs/file-nr')
        self.allocated_file_handles = 0
        self.free_file_handles = 0
        self.max_file_handles = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/sys/fs/file-nr'''
        tokens = self.content.split()
        if tokens[0]:
            self.allocated_file_handles = int(tokens[0])
        if tokens[1]:
            self.free_file_handles = int(tokens[1])
        if tokens[2]:
            self.max_file_handles = int(tokens[2])

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('Allocated file handles:', self.allocated_file_handles)
        print('Free file handles:', self.free_file_handles)
        print('Max file handles:', self.max_file_handles)
