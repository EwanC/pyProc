#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcDumpable(ProcBase):
    '''Object represents the /proc/sys/fs/suid_dumpable file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/sys/fs/suid_dumpable')
        self.core_dumps_enabled = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/sys/fs/suid_dumpable'''
        self.core_dumps_enabled = int(self.content)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        if self.core_dumps_enabled == 0:
            print('User must have read permissions for binary core dump')
        elif self.core_dumps_enabled == 1:
            print('All processes core dump when possible')
        elif self.core_dumps_enabled == 2:
            print('Binaries which are not normally dumped '
                  'are dumped readable by root only')
