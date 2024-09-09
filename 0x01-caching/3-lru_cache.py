#!/usr/bin/env python3
'''LRU(least recently used)'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Inherit from base caching parent class'''

    def __init__(self):
        '''Initializing parent class'''

        super().__init__()
        self.least_used = []

    def put(self, key, item):
        '''Least recently used'''

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
               and key not in self.cache_data:
                print('DISCARD: {}'.format(self.least_used[0]))
                del self.cache_data[self.least_used[0]]
                del self.least_used[0]
            if key in self.least_used:
                self.least_used.remove(key)
            self.least_used.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''Get item by key'''

        if key and key in self.cache_data:
            self.least_used.remove(key)
            self.least_used.append(key)
            return self.cache_data[key]
        else:
            return None
