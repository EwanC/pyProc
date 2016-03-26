#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcPidMax(ProcBase):
    '''Object represents the /proc/sys/kernel/pid_max file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/sys/kernel/pid_max')
        self.max_pid = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/sys/kernel/pid_max'''
        self.max_pid = int(self.content)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('Maximum pid {0}, after which pids wrap around'.
              format(self.max_pid))
