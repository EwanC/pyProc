#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcCmdline(ProcBase):
    '''Object represents the /proc/[pid]/cmdline file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/{0}/cmdline'.format(pid))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('Process command line:', self.content)
