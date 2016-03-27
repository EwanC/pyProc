#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcCmdline(ProcBase):
    '''Object represents the /proc/[pid]/cmdline file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        which loads the contents into self.content.
        This file is already ASCII printable, so no
        further parsing is required.
        '''
        super().__init__('/proc/{0}/cmdline'.format(pid))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        if self.content:
            print('Process command line:', self.content)
