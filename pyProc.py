#!/usr/bin/env python3

from proc_stat import ProcStat
from proc_uptime import ProcUptime


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

if __name__ == '__main__':
    print_stats()
    print_uptime()
