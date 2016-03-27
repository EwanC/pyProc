#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcStatus(ProcBase):
    '''Object represents the /proc/[pid]/status file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/{0}/status'.format(pid))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header
        if self.content:
            print(self.content)
