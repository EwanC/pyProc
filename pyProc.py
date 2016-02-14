#!/usr/bin/env python3

import os
import sys

from proc_stat import ProcStat
from proc_swaps import ProcSwaps
from proc_uptime import ProcUptime
from proc_version import ProcVersion


class PrintManager:
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
                              ProcVersion()]

    def dump_all(self):
        '''
        Iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        for _file in self.file_wrappers:
            _file.dump()  # Implemented in base class


if __name__ == '__main__':

    if os.name != 'posix':
        print('pyProc only supports UNIX systems, exiting')
        sys.exit()

    # Print all details
    printer = PrintManager()
    printer.dump_all()
