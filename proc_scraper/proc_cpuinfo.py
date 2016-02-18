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

    def dump(self):
        for deet,ail in self.details: 
            print(deet,":",ail) 
        print('\n\n')

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

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcCpuInfo, self).dump()  # Print file header

        for cpu in self.cpus:
            cpu.dump()

