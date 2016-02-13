#!/usr/bin/env python3

from proc_stat import ProcStat


def print_stats():
    '''
    Parses details from the /proc/stat file.
    Gathered information is then printed to stdout.
    '''
    stat = ProcStat()
    stat.dump()

if __name__ == '__main__':
    print_stats()
