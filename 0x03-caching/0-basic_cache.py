#!/usr/bin/python3
""" Basic dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """child class inherits from parent BaseCaching
        BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data the values for the keys"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value in self.cache_data linked to key."""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
