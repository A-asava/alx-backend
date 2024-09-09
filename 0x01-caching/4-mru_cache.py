#!/usr/bin/env python3
'''MRU(most recently used)'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''MRU(most recently used) cache system'''

    def __init__(self):
        '''Initializing a class'''

        super().__init__()
        self.most_recently_used = []

    def put(self, key, item):
        '''Most recently used'''

        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
               and key not in self.cache_data:
                print('DISCARD: {}'.format(self.most_recently_used[-1]))
                del self.cache_data[self.most_recently_used[-1]]
                del self.most_recently_used[-1]
            if key in self.most_recently_used:
                self.most_recently_used.remove(key)
            self.most_recently_used.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''Get items by key'''

        if key and key in self.cache_data:
            self.most_recently_used.remove(key)
            self.most_recently_used.append(key)
            return self.cache_data[key]
        else:
            return None
