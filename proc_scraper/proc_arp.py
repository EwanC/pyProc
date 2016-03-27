#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcARP(ProcBase):
    '''Object represents the /proc/net/arp file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        which reads the contents. This file is already
        printable ASCII, so we can print it without
        any further parsing.
        '''
        super().__init__('/proc/net/arp')

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header
        print(self.content)
