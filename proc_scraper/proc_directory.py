#!/usr/bin/env python3

# Imports for parsing files in /proc root directory
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

# Imports for parsing files in proc/sys directory
from .proc_vsyscall import ProcVSyscall
from .proc_filenr import ProcFileNR
from .proc_inodenr import ProcInodeNR
from .proc_dumpable import ProcDumpable
from .proc_pidmax import ProcPidMax
from .proc_threadmax import ProcThreadMax

# Imports for parsing files in proc/net directory
from .proc_arp import ProcARP
from .proc_net_dev import ProcNetDev
from .proc_protocols import ProcProtocols

# Imports for parsing files in proc/[pid] directory
from .proc_cmdline import ProcCmdline
from .proc_environ import ProcEnviron
from .proc_stack import ProcStack
from .proc_status import ProcStatus
from .proc_oom_score import ProcOomScore
from .proc_maps import ProcMaps
from .proc_io import ProcIO
from .proc_mounts import ProcMounts
from .proc_fdinfo import ProcFdInfo


class ProcDirectory:
    '''
    Class manages the list of supported /proc
    sub-files we have classes for.

    As well as printing the information contained in
    them to stdout.
    '''

    def dump_base(self):
        '''
        Creates instances of all the file abstractions from the root /proc
        directory, inheriting from procBase.
        Then iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        base_wrappers = [ProcStat(),
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

        for _file in base_wrappers:
            _file.dump()  # Always implemented in base class

    def dump_proc(self, pid):
        '''
        Creates instances of all the file abstractions from the /proc/[pid]
        directory, inheriting from procBase.
        Then iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        pid_wrappers = [ProcCmdline(pid),
                        ProcEnviron(pid),
                        ProcStack(pid),
                        ProcStatus(pid),
                        ProcOomScore(pid),
                        ProcMaps(pid),
                        ProcIO(pid),
                        ProcMounts(pid),
                        ProcFdInfo(pid)]

        for _file in pid_wrappers:
            _file.dump()  # Always implemented in base class

    def dump_net(self):
        '''
        Creates instances of all the file abstractions from the /proc/net
        directory, inheriting from procBase.
        Then iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        net_wrappers = [ProcARP(),
                        ProcNetDev(),
                        ProcProtocols()]

        for _file in net_wrappers:
            _file.dump()  # Always implemented in base class

    def dump_sys(self):
        '''
        Creates instances of all the file abstractions from the /proc/sys
        directory, inheriting from procBase.
        Then iterates over all files and prints their details to
        stdout using overridden procBase dump() function.
        '''
        sys_wrappers = [ProcVSyscall(),
                        ProcFileNR(),
                        ProcInodeNR(),
                        ProcDumpable(),
                        ProcPidMax(),
                        ProcThreadMax()]

        for _file in sys_wrappers:
            _file.dump()  # Always implemented in base class
