#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcVSyscall(ProcBase):
    '''Object represents the /proc/sys/abi/vsyscall32 file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/sys/abi/vsyscall32')
        self.enabled = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/sys/abi/vsyscall32'''
        self.enabled = int(self.content)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        if self.enabled == 0:
            print("IA-32 syscalls are disabled")
        else:
            print("IA-32 syscalls are enabled")
