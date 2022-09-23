#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """child class inherits from parent BaseCaching
        BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the values for the keys
           If the number of items in self.cache_data > BaseCaching.MAX_ITEMS:
           discard the least frequency used item (LFU algorithm)
           if you find more than 1 item to discard,
           use the LRU algorithm to discard only the least recently used
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                LFU_key = self.cache_data.pop()
                print("DISCARD:", LFU_key)

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
