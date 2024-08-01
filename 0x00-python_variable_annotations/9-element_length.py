#!/usr/bin/env python3
'''Module that calculates the len of a list of seq
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Calculates the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
