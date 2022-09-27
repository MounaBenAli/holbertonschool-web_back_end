#!/usr/bin/env python3
""" Simple helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[(int, int)]:
    """ Takes two integer arguments page and page_size.
        Returns a tuple of size two containing a start index
        and an end index corresponding to the range of indexes.
    """

    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return (start_index, end_index)
