#!/usr/bin/python3
"""  LRU Caching """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """child class inherits from parent BaseCaching
        BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the values for the keys
           If the number of items in self.cache_data > BaseCaching.MAX_ITEMS:
           discard the least recently used item (LRU algorithm)
        """
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                LRU_key = self.cache_data.popitem(last=False)
                print("DISCARD:", LRU_key)

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
