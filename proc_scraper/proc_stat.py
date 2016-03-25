#!/usr/bin/env python3

from .proc_base import ProcBase


class CpuStats:
    '''
    Represents a single CPU entry from the /proc/stat file.
    '''

    # Format string for a table entry
    table_format_str = '| {0:>6} | {1:>9} | {2:>5} | {3:>11} | {4:>8} |' \
                       ' {5:>11} | {6:>5} | {percent:7.2f} |'

    def __init__(self, line):
        '''
        Parse line read from /proc/stat to get CPU
        execution time breakdown.

        Keyword arguments:
        line -- A single line read from /proc/stat starting with cpu[0-9]*
        '''

        split = line.split()

        if split[0][-1].isdigit():
            self.label = '#' + split[0][-1]
            self.index = int(split[0][-1])
        else:
            self.label = 'All'
            self.index = -1

        self._entries = [int(entry) for entry in split[1:]]

    def get_total(self):
        '''
        Returns total amount of CPU time
        summed across all activities.
        '''
        return sum(self._entries)

    def dump_table_entry(self, _percent):
        '''
        Prints a single table line.

        Keyword arguments:
        _percent -- CPUs percentage of total computation time
        '''
        print(CpuStats.table_format_str.format(
            self.label, *self._entries, percent=_percent))


class ProcStat(ProcBase):
    '''Object represents the /proc/stat file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.cpus = []
        self.stats = []
        super().__init__('/proc/stat')
        self.read()

    def read(self):
        '''Parses contents of /proc/stat'''
        # Iterate over each line of the file
        for line in self.content.split('\n'):
            tokens = line.split()

            if not tokens:
                continue

            if line.startswith('cpu'):
                # Parse cpu details using CpuStats class
                self.cpus.append(CpuStats(line))
            elif tokens[0] == 'ctxt':
                self.stats.append(('Number of context switches:', tokens[-1]))
            elif tokens[0] == 'btime':
                self.stats.append(
                    ('Boot time in seconds since epoch:', tokens[-1]))
            elif tokens[0] == 'processes':
                self.stats.append(
                    ('Number of processes forked since boot:', tokens[-1]))
            elif tokens[0] == 'procs_running':
                self.stats.append(
                    ('Number of processes in a runnable state:', tokens[-1]))
            elif tokens[0] == 'procs_blocked':
                self.stats.append(
                    ('Number of processes blocked on I/O:', tokens[-1]))

    def _dump_cpu_stat_table(self):
        '''Print table of CPU time stats.'''
        table_heading_str = '| CPU ID | User Land | Niced | System Land |' \
                            '   Idle   | I/O blocked |  IRQ  |    %    |'
        print(table_heading_str)
        print('-' * len(table_heading_str))

        total_usage = max([cpu.get_total() for cpu in self.cpus])

        for cpu in self.cpus:
            percent = (cpu.get_total() / total_usage) * 100
            cpu.dump_table_entry(percent)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        for (msg, num) in self.stats:
            print(msg, num)

        print('\n')  # Double new line
        self._dump_cpu_stat_table()
