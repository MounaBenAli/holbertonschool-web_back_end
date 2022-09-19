#!/usr/bin/env python3
""" iterable object """


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Task: Annotate the function’s parameters
    and return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
