#!/usr/bin/env python3

from .proc_base import ProcBase


from math import ceil


class ProcMemInfo(ProcBase):
    '''Object represents the /proc/meminfo file.'''

    format_str = '{0:20} {1:10} {2}'

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.stats = {'MemTotal': None,
                      'MemFree': None,
                      'MemAvailable': None,
                      'Buffers': None,
                      'Cached': None,
                      'SwappedCached': None,
                      'Active': None,
                      'InActive': None,
                      'Active(anon)': None,
                      'InActive(anon)': None,
                      'Active(file)': None,
                      'InActive(file)': None,
                      'Unevictable': None,
                      'Mlocked': None,
                      'SwapTotal': None,
                      'SwapFree': None,
                      'Dirty': None,
                      'Writeback': None,
                      'AnonPages': None,
                      'Mapped': None,
                      'Shmem': None,
                      'Slab': None,
                      'SReclaimable': None,
                      'SUnreclaim': None,
                      'KernelStack': None,
                      'PageTables': None,
                      'NFS_Unstable': None,
                      'Bounce': None,
                      'WritebackTmp': None,
                      'CommitLimit': None,
                      'VmallocTotal': None,
                      'VmallocUsed': None,
                      'VmallocChunk': None,
                      'HardwareCorrupted': None,
                      'AnonHugePages': None,
                      'HugePages_Total': None,
                      'HugePages_Free': None,
                      'HugePages_Rsvd': None,
                      'HugePages_Surp': None,
                      'Hugepagessize': None,
                      'DirectMap4k': None,
                      'DirectMap2M': None}

        super().__init__('/proc/meminfo')
        self.read()

    def read(self):
        '''Parses contents of /proc/meminfo'''

        # Iterate over each file line
        for line in self.content.split('\n'):
            if not line:
                continue

            tokens = line.split()
            search_key = tokens[0]
            if search_key[-1] == ':':
                search_key = search_key[:-1]

            for attribute in self.stats:
                if attribute == search_key:
                    if tokens[1] == '0':
                        self.stats[attribute] = int(0)
                    else:
                        size = int(tokens[1])
                        if tokens[2] == 'kB':
                            size *= 1024
                        elif tokens[2] == 'mB':
                            size *= (1024 * 1024)

                        self.stats[attribute] = size

    def dump(self):
        '''Print information gathered to stdout.'''

        super().dump()  # Print file header

        # TODO - it would be nice to sort this output
        for attribute in self.stats:
            value = self.stats[attribute]
            if value == 0 or value is None:
                continue

            suffix = "bytes"
            if value >= 1024:
                value = ceil(value / 1024)
                if value >= 1024:
                    value = ceil(value / 1024)
                    if value >= 1024:
                        value = ceil(value / 1024)
                        suffix = "GB"
                    else:
                        suffix = "MB"
                else:
                    suffix = "KB"

            print(self.format_str.format(attribute, value, suffix))

        print('\n\n')
