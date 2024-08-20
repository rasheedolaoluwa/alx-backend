#!/usr/bin/python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO caching implementation """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.queue:
                last = self.queue.pop()
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            self.queue.append(key)
        else:
            self.mv_last_list(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)

    def mv_last_list(self, item):
        """ Move an element to the last index of the list """
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)
            self.queue.append(item)
