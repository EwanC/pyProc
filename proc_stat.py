#!/usr/bin/env python3

from proc_base import ProcBase

class CpuStats:

    def __init__(self, line):

        self.__entries = {'user' : 0, 'nice' : 0, 'system' : 0, 'idle' : 0, 'iowait' : 0,
                'irq' : 0, 'softirq' : 0, 'steal' :0, 'guest' : 0, 'guest_nice' : 0}

        split = line.split()

        if split[0][-1].isdigit():
            self.label = "Stats for CPU #" + split[0][-1]
        else:
            self.label = "Stats across all CPUs"

        for idx, entry in enumerate(split[1:]):
            self.__entries[idx] = entry


    def dump(self):
        print(self.label)
        for key, value in self.__entries.items():
            print("\t",key, value)

class ProcStat(ProcBase):
    
    def __init__(self):
        self.cpus=[]
        super(ProcStat, self).__init__('/proc/stat')
        self.read()

    def read(self):
        for line in self.content.split('\n'):
            if line.startswith('cpu'):
                self.cpus.append(CpuStats(line))

    def dump(self):
        for cpu in self.cpus:
            cpu.dump()

    
