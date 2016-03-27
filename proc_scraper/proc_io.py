#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcIO(ProcBase):
    '''Object represents the /proc/[pid]/io file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/{0}/io'.format(pid))
        self.io_stats = []
        self.read()

    def read(self):
        '''Parses contents of /proc/[pid]/io'''
        if not self.content:
            return

        for line in self.content.split('\n'):
            tokens = line.split()
            if not tokens:
                continue

            if tokens[0] == 'rchar:':
                msg = 'characters read, including cached data without disk'
                self.io_stats.append((msg, int(tokens[-1])))

            if tokens[0] == 'wchar:':
                self.io_stats.append(('characters written', int(tokens[-1])))

            if tokens[0] == 'syscr:':
                self.io_stats.append(('read system calls', int(tokens[-1])))

            if tokens[0] == 'syscw:':
                self.io_stats.append(('write system calls', int(tokens[-1])))

            if tokens[0] == 'read_bytes:':
                msg = 'bytes read, fetched from the storage medium'
                self.io_stats.append((msg, int(tokens[-1])))

            if tokens[0] == 'write_bytes:':
                self.io_stats.append(('bytes written', int(tokens[-1])))

            if tokens[0] == 'cancelled_write_bytes:':
                msg = 'bytes lost to truncating the pagecache'
                self.io_stats.append((msg, int(tokens[-1])))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        for (msg, value) in self.io_stats:
            print(msg, '-', value)
