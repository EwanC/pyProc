#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcStatus(ProcBase):
    '''Object represents the /proc/[pid]/status file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        which populates self.content. Since this
        file is already ASCII printable no further
        parsing is required.
        '''
        super().__init__('/proc/{0}/status'.format(pid))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        if self.content:
            print(self.content)
