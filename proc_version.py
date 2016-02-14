#!/usr/bin/env python3

from proc_base import ProcBase


class ProcVersion(ProcBase):
    '''Object represents the /proc/version file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor.
        No parsing of the file is necessary.
        '''
        super(ProcVersion, self).__init__('/proc/version')

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcVersion, self).dump()  # Print file header
        print(self.content)
