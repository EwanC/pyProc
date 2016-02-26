#!/usr/bin/env python3

from .proc_base import ProcBase


class CpuDetails:
    '''
    Class representing the information relating to
    a single cpu entry from /proc/cpu_info
    '''

    def __init__(self, cpu_lines):
        '''
        Parse several lines read from /proc/cpu_info
        for a single cpu
        '''

        self.details = { 'processor' : None,
                         'vendor_id' : None,
                         'family' : None,
                         'model#' : None,
                         'model_name' : None,
                         'vendor_id' : None,
                         'stepping' : None,
                         'microcode' : None,
                         'hertz' : None,
                         'cache_size' : None,
                         'physical_id' : None,
                         'siblings' : None,
                         'core_id' : None,
                         '#cores' : None,
                         'fpu' : None,
                         'cpu_id' : None,
                         'flags' : None,
                         'bogomips' : None,
                         'cache_alignment' : None,
                         'addr_sizes' : None,
                         'power' : None,
                }

        for line in cpu_lines.split('\n'):
            tokens = line.split()

            if not tokens:
                continue

            if tokens[0] == 'processor':
                self.details['cpu index'] = tokens[-1]
            elif tokens[0] == 'vendor_id':
                self.details['vendor_id'] = tokens[-1]
            elif tokens[0] == 'cpu' and tokens[1] == 'family':
                self.details['family'] = tokens[-1]
            elif tokens[0] == 'model' and tokens[1] == ':':
                self.details['model#'] = tokens[-1]
            elif tokens[0] == 'model' and tokens[1] == 'name':
                self.details['model name'] = tokens[2:]
            elif tokens[0] == 'stepping':
                self.details['stepping'] = tokens[-1]
            elif tokens[0] == 'microcode':
                self.details['microcode'] = tokens[-1]
            elif tokens[0] == 'cpu' and tokens[1] == 'MHz':
                self.details['hertz'] = tokens[-1]
            elif tokens[0] == 'cache':
                self.details['cache_size'] = tokens[-2]
            elif tokens[0] == 'physical':
                self.details['physical_id'] = tokens[-1]
            elif tokens[0] == 'siblings':
                self.details['siblings'] = tokens[-1]
            elif tokens[0] == 'core':
                self.details['core_id'] = tokens[-1]
            elif tokens[0] == 'cpu' and tokens[1] == 'cores':
                self.details['#cores'] = tokens[-1]
            elif tokens[0] == 'fpu' and tokens[1] == ':':
                self.details['fpu'] = tokens[-1] == 'yes'
            elif tokens[0] == 'cpuid':
                self.details['cpu_id'] = tokens[-1]
            elif tokens[0] == 'flags':
                self.details['flags'] = tokens[2:]
            elif tokens[0] == 'bogomips':
                self.details['bogomips'] = tokens[-1]
            elif tokens[0] == 'cache_alignment':
                self.details['cache_alignment'] = tokens[-1]
            elif tokens[0] == 'address':
                self.details['addr_sizes'] = tokens[3:]
            elif tokens[0] == 'power':
                self.details['power'] = tokens[1:]

    def dump(self):
        '''Print all details to stdout.'''
        for attribute, value in self.details:
            if isinstance(value, list):
                print(attribute, ": ", " ".join(value))
            else:
                print(attribute, ": ", value)
        print('\n\n')

    def __eq__(self, other):
        '''== operator overload'''
        if isinstance(other, self.__class__):
            are_same = self.details['vendor_id'] == other.details['vendor_id']
            are_same = are_same and (
                self.details['model#'] == other.details['model#'])
            are_same = are_same and (
                self.details['family'] == other.details['family'])
            return are_same
        else:
            return False

    def __ne__(self, other):
        '''!= operator overload'''
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
        '''Print a selected subset of cpu info to stdout'''
        print(" ".join(first_cpu.details['model name'][1:]) + ":")
        print("\t" + first_cpu.details['siblings'] + " CPU(s)")
        print("\t" + first_cpu.details['hertz'] + " MHz")
        print("\t" + first_cpu.details['cache_size'] + " KB Cache")
        print("\t" + first_cpu.details['bogomips'] + " bogoMips")

    def dump(self):
        '''Print information gathered to stdout.'''
        super(ProcCpuInfo, self).dump()  # Print file header

        are_identical = all(cpu == self.cpus[0] for cpu in self.cpus[1:])

        if are_identical:
            self.dump_coalesced(self.cpus[0])
        else:
            for cpu in self.cpus:
                cpu.dump()
