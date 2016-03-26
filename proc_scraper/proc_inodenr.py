#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcInodeNR(ProcBase):
    '''Object represents the /proc/sys/fs/inode-nr file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/sys/fs/inode-nr')
        self.allocated_inodes = 0
        self.free_inodes = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/sys/fs/inode-nr'''
        tokens = self.content.split()
        if tokens[0]:
            self.allocated_inodes = int(tokens[0])
        try:
            if tokens[1]:
                self.free_inodes = int(tokens[1])
        except:
            pass

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('Allocated inodes:', self.allocated_inodes)
        print('Free inodes:', self.free_inodes)
