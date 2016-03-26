#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcModules(ProcBase):
    '''Object represents the /proc/modules file.'''

    format_str = '{0:30}   {1:<10}  {2:} {3:}'

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/modules')
        self.modules = []
        self.read()

    def read(self):
        '''Parses contents of /proc/partitions'''
        for line in self.content.split('\n'):

            tokens = line.split()
            if not tokens:
                continue

            name = None
            size = 0
            use_count = 0
            referring_modules = []

            if tokens[0]:
                name = tokens[0]

            if tokens[1] and tokens[1].isdigit():
                size = int(tokens[1])

            if tokens[2] and tokens[2].isdigit():
                use_count = int(tokens[2])

            if tokens[3] != '-':
                referring_modules.append(tokens[3])

            self.modules.append((name, size, use_count, referring_modules))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        table_header_str = self.format_str.format(
                           'Name', 'Bytes', 'Use count', '')
        print(table_header_str)
        print(len(table_header_str) * '-')

        for (name, size, use_count, refs) in self.modules:
            refrenced_by = ''.join(refs)
            if refrenced_by and refrenced_by[-1] == ',':
                refrenced_by = refrenced_by[:-1]

            print(self.format_str.format(name, size, use_count, refrenced_by))
