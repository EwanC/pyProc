#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcCrypto(ProcBase):
    '''Object represents the /proc/crypto file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/crypto')
        self.ciphers = []
        self.read()

    def read(self):
        '''Parses contents of /proc/crypto'''
        for line in self.content.split('\n'):
            tokens = line.split()
            if not tokens:
                continue

            if tokens[0] == 'name' and not tokens[-1].startswith('__'):
                self.ciphers.append(tokens[-1])

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('Ciphers used by the kernel:\n')
        for cipher in self.ciphers:
            print(cipher)
