#!/usr/bin/env python3
'''LIFO caching'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO caching system'''

    def __init__(self):
        '''Initializing parent class'''

        super().__init__()
        self.data_cache = []

    def put(self, key, item):
        '''insert item'''

        if key is None or item is None:
            pass
        else:
            len_data = len(self.cache_data)
            if len_data >= BaseCaching.MAX_ITEMS\
               and key not in self.cache_data:
                print('DISCARD: {}'.format(self.data_cache[-1]))
                del self.cache_data[self.data_cache[-1]]
                del self.data_cache[-1]
            self.data_cache.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''Get item by key'''

        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
