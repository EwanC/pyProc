#!/usr/bin/env python3

from proc_base import ProcBase

class CpuStats:

    def __init__(self, line):

        self.__entries = {'user' : 0, 'nice' : 0, 'system' : 0, 'idle' : 0, 'iowait' : 0,
                          'irq' : 0, 'softirq' : 0, 'steal' :0, 'guest' : 0, 'guest_nice' : 0}


        split = line.split()

        if split[0][-1].isdigit():
            self.label = "Stats for CPU #" + split[0][-1]
            self.index = int(split[0][-1])
        else:
            self.label = "Stats across all CPUs"
            self.index = -1

        self.__entries['user'] = int(split[1])
        self.__entries['nice'] = int(split[2])
        self.__entries['system'] = int(split[3])
        self.__entries['idle'] = int(split[4])
        self.__entries['iowait'] = int(split[5])
        self.__entries['irq'] = int(split[6])
        self.__entries['softirq'] = int(split[7])
        self.__entries['steal'] = int(split[8])
        self.__entries['guest'] = int(split[9])
        self.__entries['guest_nice'] = int(split[10])

    def dump(self):
        print(self.label)
        for key, value in self.__entries.items():
            print("\t",key, value)

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

    def dump(self):
        super(ProcStat, self).dump()

        for (msg,num) in self.stats:
           print(msg, num)

        for cpu in self.cpus:
            cpu.dump()
