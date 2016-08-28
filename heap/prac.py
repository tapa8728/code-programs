import heapq
from heapq import *

class Heap(object):

	def __init__(self):
		self.hh = list()

	def insert(self, val):
		if heappush(self.hh, val):
			print "{} successfully added into the heap".format(val)

	def remove(self, val):
		try:
			if val == self.hh[0]:
				self.hh.remove(val)
				heapify(self.hh) # only heapify if the element removed was the root of the heap
			else:
				self.hh.remove(val)
			print "{} successfully removed from the heap".format(val)		
		except:
			print "{} does not exist in the heap".format(val)

	def getMin(self):
		print "Min in {}".format(self.hh[0])

	def getLargest(self, n):
		print "Largest {}".format(nlargest(n, self.hh)[-1])

	def getSmallest(self, n):
		print "Smallest {}".format(nsmallest(n, self.hh)[-1])

h = Heap()
h.insert(19)
h.insert(32)
h.insert(1)
h.insert(78)
print h.hh
h.getMin()
h.getSmallest(2)
h.getLargest(2)
h.remove(19)
h.remove(1)
print h.hh

