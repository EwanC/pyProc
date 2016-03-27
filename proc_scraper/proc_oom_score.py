#!/usr/bin/env python3

from .proc_base import ProcBase


class ProcOomScore(ProcBase):
    '''Object represents the /proc/[pid]/oom_score file.'''

    def __init__(self, pid):
        '''
        Read file by calling base class constructor
        then parse the contents.
        '''
        super().__init__('/proc/{0}/oom_score'.format(pid))
        self.oom_score = 0
        self.read()

    def read(self):
        '''Parses contents of /proc/[pid]/oom_score'''
        if self.content:
            self.oom_score = int(self.content)

    def dump(self):
        '''Print information gathered to stdout.'''
        super().dump()  # Print file header

        print('OMM score:', self.oom_score)
        print('A higher score means that the process is more likely to be')
        print('selected by the OOM-killer when trying to free up memory')
