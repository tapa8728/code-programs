'''

Create a data structure that supports these functions: 
insert(int val),
 getRandom(), 
 delete(int val) in O(1) time.


 Dictionaries: dict and defaultdict
                               Complexity
Operation     | Example      | Class         | Notes
--------------+--------------+---------------+-------------------------------
Index         | d[k]         | O(1)	     |
Store         | d[k] = v     | O(1)	     |
Length        | len(d)       | O(1)	     |
Delete        | del d[k]     | O(1)	     |
get/setdefault| d.method     | O(1)	     |
Pop           | d.pop(k)     | O(1)	     |
Pop item      | d.popitem()  | O(1)	     |
Clear         | d.clear()    | O(1)	     | similar to s = {} or = dict()
Views         | d.keys()     | O(1)	     |

Construction  | dict(...)    | O(len(...))   | depends # (key,value) 2-tuples

Iteration     | for k in d:  | O(N)          | all forms: keys, values, items

So, most dict operations are O(1).

'''
from timeit import timeit
import random
import collections
from collections import defaultdict


class EfficientDS(object):

	def __init__(self):
		self.ds = defaultdict(int)

	## insert O(1)
	def insert(self, val):
		self.ds[val]

	## delete O(1)
	def delete(self, val):
		try:
			del self.ds[val]
			return True
		except Exception, e:
			return False
			
	## get random element
	def random(self):
		print random.choice(self.ds.keys())


print "Construction"
firstDS = EfficientDS()

print "insertion"
firstDS.insert(5)
firstDS.insert(12)
firstDS.insert(62)

print "delete"
firstDS.delete(5)

print "get random"
firstDS.random()
firstDS.random()

print firstDS.ds


