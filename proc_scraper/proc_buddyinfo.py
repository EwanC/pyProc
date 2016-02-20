#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcBuddyInfo(ProcBase):
    '''Object represents the /proc/buddyinfo file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.lines = []
        super(ProcBuddyInfo, self).__init__('/proc/buddyinfo')
        self.read()

    def read(self):
        '''Parses contents of /proc/buddyinfo'''
        lines = self.content.split('\n')

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcBuddyInfo, self).dump()  # Print file header

        print('//TODO buddy info description here\n')

        for line in self.lines:
            print(line)
