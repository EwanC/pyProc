#!/usr/bin/env python3

from .proc_base import ProcBase

import os


class ProcBuddyInfo(ProcBase):
    '''Object represents the /proc/buddyinfo file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.nodes = []
        super(ProcBuddyInfo, self).__init__('/proc/buddyinfo')
        self.read()

    def read(self):
        '''Parses contents of /proc/buddyinfo'''
        for line in self.content.split('\n'):
            tokens = line.split()

            if not tokens:
                continue

            if tokens[0] == 'Node':
                node = int(tokens[1].strip(','))
            if tokens[2] == 'zone':
                zone = tokens[3]
            chunks = tokens[4:]

            self.nodes.append((node,zone,chunks))

    def get_fragment_magnitudes(self, chunks):
        entries = len(chunks)
        page_size = os.sysconf("SC_PAGE_SIZE")
        return [page_size * (2 ** order) for order in range(0,entries)]

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcBuddyInfo, self).dump()  # Print file header

        print('//TODO buddy info description here\n')
       
        for node, zone, chunks in self.nodes:
            heading = 'Node {0}, Zone {1}'.format(node, zone)
            print(heading)
            print('*' * len(heading))
           
            print('\tChunk size(Bytes)        Free chunks           Total KB')

            entries = self.get_fragment_magnitudes(chunks)
            total_bytes = 0
            for e,c in zip(entries,chunks):
                bytes_used = int(e) * int(c)
                total_bytes += bytes_used
                print('\t{0:<24} {1:<21} {2}'.format(e,c,bytes_used/1024))


            print('\n\tTotal KB:',total_bytes/1024,'\n')
