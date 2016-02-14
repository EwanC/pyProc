#!/usr/bin/env python3

from proc_stat import ProcStat
from proc_uptime import ProcUptime
from proc_version import ProcVersion
from proc_swaps import ProcSwaps


def print_stats():
    '''
    Parses details from the /proc/stat file.
    Gathered information is then printed to stdout.
    '''
    stat = ProcStat()
    stat.dump()


def print_uptime():
    '''
    Parses details from the /proc/uptime file.
    Gathered information is then printed to stdout.
    '''
    uptime = ProcUptime()
    uptime.dump()


def print_version():
    '''
    Parses details from the /proc/version file.
    Gathered information is then printed to stdout.
    '''
    version = ProcVersion()
    version.dump()


def print_swaps():
    '''
    Parses details from the /proc/swaps file.
    Gathered information is then printed to stdout.
    '''
    swaps = ProcSwaps()
    swaps.dump()


if __name__ == '__main__':
    print_stats()
    print_uptime()
    print_version()
    print_swaps()
