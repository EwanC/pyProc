#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcFileSystems(ProcBase):
    '''Object represents the /proc/filesystem file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.file_systems = []
        super(ProcFileSystems, self).__init__('/proc/filesystems')
        self.read()

    def read(self):
        '''Parses contents of /proc/filesystems'''

        # Iterate over each line of the file
        for line in self.content.split('\n')[1:]:
            tokens = line.split()

            if not tokens:
                continue

            self.file_systems.append(tokens[-1])

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcFileSystems, self).dump()  # Print file header

        print('File systems supported by the kernel:')

        for fs in self.file_systems:
            print(fs)
