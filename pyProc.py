#!/usr/bin/env python3

from proc_stat import ProcStat


def print_stats():
    stat = ProcStat()
    stat.dump()

if __name__ == '__main__':
    print_stats()
