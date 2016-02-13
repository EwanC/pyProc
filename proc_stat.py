#!/usr/bin/env python3

from proc_base import ProcBase

class CpuStats:

    table_format_str = "| {0:>6} | {1:>9} | {2:>5} | {3:>10} | {4:>9} | {5:>11} | {6:>5} |"
    
    def __init__(self, line):

        self.__entries = []
        split = line.split()

        if split[0][-1].isdigit():
            self.label = "#" + split[0][-1] 
            self.index = int(split[0][-1])
        else:
            self.label = "All"
            self.index = -1

        self.user = int(split[1])
        self.nice = int(split[2])
        self.system = int(split[3])
        self.idle = int(split[4])
        self.io = int(split[5])
        self.irq = int(split[6])

    def dump_table_entry(self):
        table_entry_str = CpuStats.table_format_str.format(
                self.label,
                self.user,
                self.nice,
                self.system,
                self.idle,
                self.io,
                self.irq)

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
        table_heading_str = "| CPU ID | User Land | Niced | System Land |   Idle   | I/O blocked |  IRQ  |"
        print(table_heading_str)
        print('-' * len(table_heading_str))
        
        for cpu in self.cpus:
            cpu.dump_table_entry()

    def dump(self):
        super(ProcStat, self).dump()

        for (msg,num) in self.stats:
           print(msg, num)

        print('\n') # double new line
        self._dump_cpu_stat_table() 
