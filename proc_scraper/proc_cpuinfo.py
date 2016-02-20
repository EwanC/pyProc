#!/usr/bin/env python3

from .proc_base import ProcBase


class CpuDetails:

    def __init__(self, cpu_lines):

       self.details = []
       for line in cpu_lines.split('\n'):
          tokens = line.split()

          if not tokens:
              continue

          if tokens[0] == 'processor':
              self.details.append(('cpu index',tokens[-1]))
          elif tokens[0] == 'vendor_id':
              self.details.append(('vendor_id',tokens[-1]))
          elif tokens[0] == 'cpu' and tokens[1] == 'family':
              self.details.append(('family',tokens[-1]))
          elif tokens[0] == 'model' and tokens[1] == ':':
              self.details.append(('model#',tokens[-1]))
          elif tokens[0] == 'model' and tokens[1] == 'name':
              self.details.append(('model name',tokens[2:]))
          elif tokens[0] == 'stepping':
              self.details.append(('stepping',tokens[-1]))
          elif tokens[0] == 'microcode':
              self.details.append(('microcode',tokens[-1]))
          elif tokens[0] == 'cpu' and tokens[1] == 'MHz':
              self.details.append(('hertz',tokens[-1]))
          elif tokens[0] == 'cache':
              self.details.append(('cache_size',tokens[-2]))
          elif tokens[0] == 'physical':
              self.details.append(('physical_id',tokens[-1]))
          elif tokens[0] == 'siblings':
              self.details.append(('siblings',tokens[-1]))
          elif tokens[0] == 'core':
              self.details.append(('core_id',tokens[-1]))
          elif tokens[0] == 'cpu' and tokens[1] == 'cores':
              self.details.append(('#cores',tokens[-1]))
          elif tokens[0] == 'fpu' and tokens[1] == ':':
              self.details.append(('fpu',tokens[-1] == 'yes'))
          elif tokens[0] == 'cpuid':
              self.details.append(('cpu_id',tokens[-1]))
          elif tokens[0] == 'flags':
              self.details.append(('flags',tokens[2:]))
          elif tokens[0] == 'bogomips':
              self.details.append(('bogomips',tokens[-1]))
          elif tokens[0] == 'cache_alignment':
              self.details.append(('cache_alignment',tokens[-1]))
          elif tokens[0] == 'address':
              self.address_sizes = tokens[3:]
              self.details.append(('addr_sizes',tokens[3:]))
          elif tokens[0] == 'power':
              self.details.append(('power',tokens[1:]))

    def find(self, attribute):
        for deet,ail in self.details: 
            if attribute == deet:
                return ail

        return None
        
          
    def dump(self):
        for deet,ail in self.details: 
            print(deet,":",ail) 
        print('\n\n')

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            are_same = self.find('vendor_id') == other.find('vendor_id')
            are_same = are_same and (self.find('model#') == other.find('model#'))
            are_same = are_same and (self.find('family') == other.find('family'))
            return are_same
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

class ProcCpuInfo(ProcBase):
    '''Object represents the /proc/cpuinfo file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.cpus = []
        self.stats = []
        super(ProcCpuInfo, self).__init__('/proc/cpuinfo')
        self.read()

    def read(self):
        '''Parses contents of /proc/cpuinfo'''
        # Iterate over each CPU
        for cpu_lines in self.content.split('\n\n'):
            if not cpu_lines:
                continue
            self.cpus.append(CpuDetails(cpu_lines))


    def dump_coalesced(self, first_cpu):
        
        print(" ".join(first_cpu.find('model name')[1:]) + ":")
        print("\t" + first_cpu.find('siblings') + " CPU(s)")
        print("\t" + first_cpu.find('hertz') + " MHz")
        print("\t" + first_cpu.find('cache_size') + " KB Cache")
        print("\t" + first_cpu.find('bogomips') + " bogoMips")


    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcCpuInfo, self).dump()  # Print file header

        are_identical = all(cpu == self.cpus[0] for cpu in self.cpus[1:])

        if are_identical:
            self.dump_coalesced(self.cpus[0])
        else:
            for cpu in self.cpus:
                cpu.dump()
