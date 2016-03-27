#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcSwaps(ProcBase):
    '''Object represents the /proc/swaps file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.swap_files = []
        super().__init__('/proc/swaps')
        self.read()

    def read(self):
        '''Parses contents of /proc/swaps'''
        for line in self.content.split('\n')[1:]:
            tokens = line.split()

            if not line.startswith(r'/dev') or len(tokens) != 5:
                continue

            self.swap_files.append(tuple(tokens))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('* When multiple swap files are available the lower the priority'
              ', the more likely the swap file will be used.\n')

        for (_name, _type, _size, _used, _priority) in self.swap_files:
            print(_name + ':')
            print('\t', 'Swap type:', _type)
            print('\t', 'Bytes available:', _size)
            print('\t', 'Bytes used:', _used)
            print('\t', '*Priority:', _priority)
