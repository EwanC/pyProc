#!/usr/bin/env python3

from proc_base import ProcBase

class CpuStats:

    table_format_str = "| {0:>6} | {1:>9} | {2:>5} | {3:>10} | {4:>9} | {5:>11} | {6:>5} | {percent:7.2f} |"
    
    def __init__(self, line):

        split = line.split()

        if split[0][-1].isdigit():
            self.label = "#" + split[0][-1] 
            self.index = int(split[0][-1])
        else:
            self.label = "All"
            self.index = -1

        self._entries = [ int(entry) for entry in split[1:]]

    def get_total(self):
        return sum(self._entries)

    def dump_table_entry(self, _percent):
        table_entry_str = CpuStats.table_format_str.format(self.label, *self._entries, percent=_percent)
        print(table_entry_str)

class ProcStat(ProcBase):
    
    def __init__(self):
        self.cpus = []
        self.stats = []
        super(ProcStat, self).__init__('/proc/stat')
        self.read()

    def read(self):
        for line in self.content.split('\n'):
            tokens = line.split()

            if not tokens:
               continue

            if line.startswith('cpu'):
                self.cpus.append(CpuStats(line))
            elif tokens[0] == 'ctxt':
                self.stats.append(('Number of context switches:', tokens[-1]))
            elif tokens[0] == 'btime':
                self.stats.append(('Boot time in seconds since epoch:', tokens[-1]))
            elif tokens[0] == 'processes':
                self.stats.append(('Number of processes forked since boot:', tokens[-1]))
            elif tokens[0] == 'procs_running':
                self.stats.append(('Number of processes in a runnable state:', tokens[-1]))
            elif tokens[0] == 'procs_blocked':
                self.stats.append(('Number of processes blocked waiting on I/O:', tokens[-1]))

    def _dump_cpu_stat_table(self):
        table_heading_str = "| CPU ID | User Land | Niced | System Land |   Idle   | I/O blocked |  IRQ  |    %    |"
        print(table_heading_str)
        print('-' * len(table_heading_str))

        total_usage = max([cpu.get_total() for cpu in self.cpus])
        
        for cpu in self.cpus:
            percent = (cpu.get_total() / total_usage) * 100
            cpu.dump_table_entry(percent)

    def dump(self):
        super(ProcStat, self).dump()

        for (msg,num) in self.stats:
           print(msg, num)

        print('\n') # double new line
        self._dump_cpu_stat_table() 
