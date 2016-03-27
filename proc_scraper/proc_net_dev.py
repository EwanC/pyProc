#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcNetDev(ProcBase):
    '''Object represents the /proc/net/dev file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/net/dev')

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header
        print(self.content)
