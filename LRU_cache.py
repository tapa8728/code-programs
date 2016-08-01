'''
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and set.

get(key) - 
---------------------
Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

set(key, value) -
--------------------- 
Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

'''

import collections
from collections import *

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict() # maintains the order of insertion

    def __repr__(self):
    	return "{} ".format(self.cache) 

    def get(self, key):
        if key in self.cache:
            value = self.cache.pop(key) # remove the key,value pair
            self.cache[key] = value #  re-add it to maintain order
            return value
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        else: #key does not exist
            if len(self.cache) >= self.capacity: #if cache is full
                self.cache.popitem(last=False) #last=False makes it pop items in a FIFO order
        #now add the new key,value pair
        self.cache[key] = value

lru = LRUCache(3)
lru.set(1, "tipsy")
lru.set(4, "reema")
print lru
lru.set(5, "booya")
print lru
print "getting--",lru.get(1)
lru.set(6, "jxxx")
print lru
