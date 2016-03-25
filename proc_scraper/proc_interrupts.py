#!/usr/bin/env python3

from .proc_base import ProcBase


class IRQList:
    '''
    List holding all the irq frequencies for a
    single CPU core
    '''

    def __init__(self, cpu_id):
        '''Give instance a CPU id'''
        self.cpu_id = cpu_id
        self.irqs = []

    def add_irq(self, irq_id, count):
        '''Add an irq and it's frequency to the list'''
        self.irqs.append((irq_id, count))

    def dump(self):
        '''Print out the list of irqs as a table to stdout'''

        heading = 'IRQ  | CPU {0} Frequency '.format(self.cpu_id)
        print(heading)
        print('-' * len(heading))

        format_str = '{0:5}| {1}'
        for (irq_name, count) in self.irqs:
            if not count == 0:
                print(format_str.format(irq_name, count))
        print()


class ProcInterrupts(ProcBase):
    '''Object represents the /proc/interrupts file.'''

    def __init__(self):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        self.cpu_irqs = []
        self.num_cpus = 0
        super().__init__('/proc/interrupts')
        self.read()

    def read(self):
        '''Parses contents of /proc/interrupts'''
        # Iterate over each CPU
        lines = self.content.split('\n')

        for cpu_id in lines[0].split():
            if not cpu_id:
                continue
            if cpu_id.startswith('CPU'):
                self.cpu_irqs.append(IRQList(cpu_id[-1]))

        for irq_line in lines[1:]:
            if not irq_line:
                continue

            tokens = irq_line.split()
            if not tokens:
                continue

            irq_id = tokens[0][:-1]  # Drop trailing colon

            cpu_counter = 1
            for cpu in self.cpu_irqs:
                try:
                    count = int(tokens[cpu_counter])
                except IndexError:
                    count = 0
                cpu_counter += 1
                cpu.add_irq(irq_id, count)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        for cpu in self.cpu_irqs:
            cpu.dump()
