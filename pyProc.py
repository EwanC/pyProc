#!/usr/bin/env python3

import os
import sys

from proc_directory import ProcDirectory


if __name__ == '__main__':

    if os.name != 'posix':
        print('pyProc only supports UNIX systems, exiting')
        sys.exit()

    # Print all details
    proc_dir = ProcDirectory()
    proc_dir.dump_all()
