#!/usr/bin/env python3

import argparse
import os
import sys

from proc_scraper.proc_directory import ProcDirectory


if __name__ == '__main__':

    if os.name != 'posix':
        print('pyProc only supports UNIX systems, exiting')
        sys.exit()

    # Parse CLI arguments
    parser = argparse.ArgumentParser(prog='pyProc')
    parser.add_argument('-p', '--pid', type=int,
                        help='Display details for /proc/[pid]. '
                              'Use pid 0 for /proc/self.')

    parser.add_argument('-n', '--net', action='store_true',
                        help='Display information from /proc/net')

    parser.add_argument('-s', '--sys', action='store_true',
                        help='Display information from /proc/sys')

    args = parser.parse_args()

    proc_dir = ProcDirectory()
    if args.pid == 0:
        proc_dir.dump_proc('self')
    elif args.pid:
        proc_dir.dump_proc(args.pid)
    if args.net:
        proc_dir.dump_net()
    if args.sys:
        proc_dir.dump_sys()

    # Print details from root /proc dir
    if len(sys.argv) == 1:
        proc_dir.dump_base()
