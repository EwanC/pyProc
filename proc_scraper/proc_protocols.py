#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcProtocols(ProcBase):
    '''Object represents the /proc/net/protocols file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/net/protocols')

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header
        print(self.content)
