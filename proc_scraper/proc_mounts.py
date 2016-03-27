#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcMounts(ProcBase):
    '''Object represents the /proc/interrupts file.'''

    format_str = '{0:15} | {1:25} | {2:15} | {3}'

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/{0}/mounts'.format(pid))
        self.mounts = []
        self.read()

    def read(self):
        '''Parses contents of /proc/[pid]/mounts'''
        if not self.content:
            return

        for line in self.content.split('\n'):
            tokens = line.split()
            if not tokens:
                continue

            name = None
            mount_point = None
            fs_type = None
            options = None

            if tokens[0]:
                name = tokens[0]
            if tokens[1]:
                mount_point = tokens[1]
            if tokens[2]:
                fs_type = tokens[2]
            if tokens[3]:
                options = tokens[3]
            self.mounts.append((name, mount_point, fs_type, options))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        table_header_str = self.format_str.format(
                'Name', 'mount point', 'file type', 'configuration')
        print(table_header_str)
        print(len(table_header_str) * '-')

        for (name, mount, fs_type, config) in self.mounts:
            print(self.format_str.format(name, mount, fs_type, config))
