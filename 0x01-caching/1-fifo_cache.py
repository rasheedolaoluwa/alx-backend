#!/usr/bin/python3
"""FIFO Caching implementation."""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching class."""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = self.get_first_list(self.queue)
            if first:
                self.queue.pop(0)
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """Retrieve an item from the cache."""
        return self.cache_data.get(key)

    def mv_last_list(self, item):
        """Move an item to the end of the queue."""
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)

    @staticmethod
    def get_first_list(array):
        """Return the first element of the list or None."""
        return array[0] if array else None
