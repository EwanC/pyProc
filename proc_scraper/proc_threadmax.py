#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcThreadMax(ProcBase):
    '''Object represents the /proc/sys/kernel/threads-max file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/sys/kernel/threads-max')
        self.max_threads = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/sys/kernel/threads-max'''
        self.max_threads = int(self.content)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('System wide maximum number of threads',
              self.max_threads)
