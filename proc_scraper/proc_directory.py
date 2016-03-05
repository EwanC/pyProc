#!/usr/bin/env python3

from .proc_stat import ProcStat
from .proc_swaps import ProcSwaps
from .proc_uptime import ProcUptime
from .proc_version import ProcVersion
from .proc_cpuinfo import ProcCpuInfo
from .proc_buddyinfo import ProcBuddyInfo
from .proc_crypto import ProcCrypto


class ProcDirectory:
    '''
    Class manages the list of supported /proc
    sub-files we have classes for.

    As well as printing the information contained in
    them to stdout.
    '''

    def __init__(self):
        '''
        Creates an instance of all the classes derived
        from ProcBase. Representing abstractions of
        the supported sub-files.
        '''
        self.file_wrappers = [ProcStat(),
                              ProcSwaps(),
                              ProcUptime(),
                              ProcVersion(),
                              ProcBuddyInfo(),
                              ProcCpuInfo(),
                              ProcCrypto()]

    def dump_all(self):
        '''
        Iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        for _file in self.file_wrappers:
            _file.dump()  # Implemented in base class
