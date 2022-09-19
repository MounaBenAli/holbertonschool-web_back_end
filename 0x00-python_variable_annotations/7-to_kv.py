#!/usr/bin/env python3
""" Complex types - string and int/float to tuple """


from typing import List, Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ type-annotated function to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple.
    """
    return (k, v * v)
