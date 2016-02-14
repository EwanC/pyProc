#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcUptime(ProcBase):
    '''Object represents the /proc/uptime file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super(ProcUptime, self).__init__('/proc/uptime')
        self.read()

    def read(self):
        '''Parses contents of /proc/uptime'''
        tokens = self.content.split()
        self.uptime = float(tokens[0])
        self.idletime = float(tokens[1])

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcUptime, self).dump()  # Print file header

        print('System uptime: {0} seconds, idle time: {1} seconds'.format(
              self.uptime, self.idletime))
