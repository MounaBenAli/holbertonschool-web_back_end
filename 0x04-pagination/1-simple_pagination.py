#!/usr/bin/env python3
""" Simple pagination """

import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Takes two integer arguments page with default value 1
           and page_size with default value 10.
           Returns empty list if input arguments are out of range,
           else returns the appropriate page of the dataset
           (i.e. the correct list of rows).
       """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index > len(self.dataset()):
            return []
        return self.dataset()[start_index:end_index]


def index_range(page: int, page_size: int) -> Tuple[(int, int)]:
    """ Takes two integer arguments page and page_size.
        Returns a tuple of size two containing a start index
        and an end index corresponding to the range of indexes.
    """

    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return (start_index, end_index)
