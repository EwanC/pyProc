#!/usr/bin/env python3

from .proc_stat import ProcStat
from .proc_swaps import ProcSwaps
from .proc_uptime import ProcUptime
from .proc_version import ProcVersion
from .proc_cpuinfo import ProcCpuInfo
from .proc_buddyinfo import ProcBuddyInfo
from .proc_crypto import ProcCrypto
from .proc_filesystems import ProcFileSystems
from .proc_interrupts import ProcInterrupts
from .proc_meminfo import ProcMemInfo
from .proc_partitions import ProcPartitions
from .proc_modules import ProcModules

from .proc_vsyscall import ProcVSyscall
from .proc_filenr import ProcFileNR
from .proc_inodenr import ProcInodeNR
from .proc_dumpable import ProcDumpable
from .proc_pidmax import ProcPidMax
from .proc_threadmax import ProcThreadMax

from .proc_arp import ProcARP
from .proc_net_dev import ProcNetDev
from .proc_protocols import ProcProtocols

from .proc_cmdline import ProcCmdline
from .proc_environ import ProcEnviron


class ProcDirectory:
    '''
    Class manages the list of supported /proc
    sub-files we have classes for.

    As well as printing the information contained in
    them to stdout.
    '''

    def __init__(self):
        '''
        Creates an instance of all the classes derived
        from ProcBase. Representing abstractions of
        the supported sub-files.
        '''
        self.base_wrappers = [ProcStat(),
                              ProcSwaps(),
                              ProcUptime(),
                              ProcVersion(),
                              ProcBuddyInfo(),
                              ProcCpuInfo(),
                              ProcMemInfo(),
                              ProcFileSystems(),
                              ProcCrypto(),
                              ProcInterrupts(),
                              ProcPartitions(),
                              ProcModules()]

        self.sys_wrappers = [ProcVSyscall(),
                             ProcFileNR(),
                             ProcInodeNR(),
                             ProcDumpable(),
                             ProcPidMax(),
                             ProcThreadMax()]

        self.net_wrappers = [ProcARP(),
                             ProcNetDev(),
                             ProcProtocols()]

    def dump_base(self):
        '''
        Iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        for _file in self.base_wrappers:
            _file.dump()  # Implemented in base class

    def dump_proc(self, pid):
        pid_wrappers = [ProcCmdline(pid),
                        ProcEnviron(pid)]

        for _file in pid_wrappers:
            _file.dump()  # Implemented in base class

    def dump_net(self):
        for _file in self.net_wrappers:
            _file.dump()  # Implemented in base class

    def dump_sys(self):
        for _file in self.sys_wrappers:
            _file.dump()  # Implemented in base class

    def dump_devices(self):
        # TODO
        print('devices')
