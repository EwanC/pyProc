#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcEnviron(ProcBase):
    '''Object represents the /proc/[pid]/environ file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/{0}/environ'.format(pid))
        self.envs = []
        self.read()

    def read(self):
        '''Parses contents of /proc/[pid]/environ'''
        if not self.content:
            return

        # Environmental variable list is null delimited
        envs = self.content.split('\0')
        for env in envs:
            self.envs.append(env)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        for e in self.envs:
            print(e)
