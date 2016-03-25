#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcPartitions(ProcBase):
    '''Object represents the /proc/partitions file.'''

    table_header_str = 'Name   major/minor ID     # KB blocks'
    format_str = '{0:4}   {1:>3}.{2:<13}  {3:}'

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/partitions')
        self.partitions = []
        self.read()

    def read(self):
        '''Parses contents of /proc/partitions'''
        for line in self.content.split('\n')[1:]:
            tokens = line.split()
            if not tokens:
                continue

            major = 0
            minor = 0
            blocks = 0
            name = None

            if tokens[0] and tokens[0].isdigit():
                major = int(tokens[0])

            if tokens[1] and tokens[1].isdigit():
                minor = int(tokens[1])

            if tokens[2] and tokens[2].isdigit():
                blocks = int(tokens[2])

            if tokens[3]:
                name = tokens[3]

            self.partitions.append((major, minor, blocks, name))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('Major devices with the same number are all '
              'controlled by the same driver.')
        print('For all SCSI drivers this is 8.\n')
        print(self.table_header_str)
        print(len(self.table_header_str) * '-')

        for (major, minor, blocks, name) in self.partitions:
            print(self.format_str.format(name, major, minor, blocks))
