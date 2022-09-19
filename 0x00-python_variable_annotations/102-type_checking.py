#!/usr/bin/env python3
""" More involved type annotations """


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Task: Use mypy to validate the following piece of code
    and apply any necessary changes."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
