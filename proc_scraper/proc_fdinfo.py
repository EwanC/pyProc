#!/usr/bin/env python3

from os import listdir

from .proc_base import ProcBase


class ProcFdInfo(ProcBase):
    '''Object represents the /proc/[pid]/fdinfo directory.'''

    format_str = '{0:12} | {1:12} | {2}'

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        directory = '/proc/{0}/fdinfo'.format(pid)
        self.open_fds = []
        self.file_path = directory
        try:
            files = listdir(directory)
        except FileNotFoundError:
            return

        for f in files:
            try:
                handle = open(directory + '/' + f, 'r')
            except FileNotFoundError:
                continue

            content = handle.read()
            position = 0
            flags = 0
            for line in content.split('\n'):
                tokens = line.split()
                if not tokens:
                    continue

                if tokens[0] == 'pos:':
                    position = int(tokens[-1])
                if tokens[0] == 'flags:':
                    flags = int(tokens[-1], 8)

            self.open_fds.append((f, position, flags))

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        table_header_str = self.format_str.format(
                           'File desc', 'offset', 'flags')
        print(table_header_str)
        print(len(table_header_str) * '-')

        for (fd, position, flags) in self.open_fds:

            # Only check first 2 byes
            flag_strs = []

            if (flags & 0x00FF) | 0x0000 == 0x0000:
                flag_strs.append('O_RDONLY')

            if flags & 0x0001 == 0x0001:
                flag_strs.append('O_WRONLY')

            if flags & 0x0002 == 0x0002:
                flag_strs.append('O_RDWR')

            if flags & 0x0003 == 0x0003:
                flag_strs.append('O_ACCMODE')

            if flags & 0x0004 == 0x0004:
                flag_strs.append('O_BINARY')

            if flags & 0x0008 == 0x0008:
                flag_strs.append('O_TEXT')

            if flags & 0x0080 == 0x0080:
                flag_strs.append('O_NOINHERIT')

            if flags & 0x0100 == 0x0100:
                flag_strs.append('O_CREAT')

            if flags & 0x0200 == 0x0200:
                flag_strs.append('O_EXCL')

            if flags & 0x0400 == 0x0400:
                flag_strs.append('O_NOCTTY')

            if flags & 0x0800 == 0x0800:
                flag_strs.append('O_TRUNC')

            if flags & 0x1000 == 0x1000:
                flag_strs.append('O_APPEND')

            if flags & 0x2000 == 0x2000:
                flag_strs.append('O_NONBlOCK')

            if flags & 0x8000 == 0x8000:
                flag_strs.append('O_LARGEFILE')

            print(self.format_str.format(fd, position, ', '.join(flag_strs)))
