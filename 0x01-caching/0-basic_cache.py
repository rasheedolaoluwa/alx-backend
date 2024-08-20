#!/usr/bin/python3
"""Basic Dictionary implementation using BaseCaching."""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that stores items in a cache."""

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key)
