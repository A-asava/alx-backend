#!/usr/bin/env python3
'''Basic dictionary'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Caching system that inherits from BaseCaching'''

    def __init__(self):
        '''Initializing parent class'''

        BaseCaching.__init__(self)

    def put(self, key, item):
        '''Does nothing'''

        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''return the value in self.cache_data linked to key'''

        if key is None or key not in self.cache_data:
            return None
        else:
            return self.cache_data[key]
