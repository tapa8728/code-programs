import collections
from random import random

class Stack(object):

	def __init__(self,lis):
		self.stck = lis

	def __repr__(self):
		return "Printing Stack ... {}".format(self.stck)

	def __getitem__(self,index):
		return self.stck[index]

	def __missing__(self, key):
		return None	

	def push_(self, item):
		self.stck.append(item)
		print "{} has been pushed successfully".format(item)

	def pop_(self):
		try:
			self.stck.pop()
			print "After popping stack is now {}".format(self.stck)
		except:
			print "Stack is empty. Cannot pop!"

	def min_(self):
		return min(self.stck)

s = Stack([-100*random() for each in range(5)])
s.pop_()
s.push_(2)
s.push_(82)
s.push_(12)
s.push_(27)
s.push_(200)
s.push_('b')
s.pop_()
print "Minimum element is - {}".format(s.min_())
#print s[1000]