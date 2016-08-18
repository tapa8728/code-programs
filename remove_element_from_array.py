'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:
	Try two pointers.
	Did you use the property of "the order of elements can be changed"?
	What happens when the elements to remove are rare?


'''
class remElement(object):
	def __init__(self, arr):
		self.ipList = arr

	def __str__(self):
		return "{}".format(self.ipList)

	def countVal(self):
		return len(self.ipList)

	# 'n' is the element whose all instances need to be removed
	def remLogic(self, n):
		print "Initial count is {}".format(self.countVal())
		self.ipList.sort()	#order can be changed
		while n in self.ipList:
			self.ipList.remove(n)

		print "Final count is {}".format(self.countVal())

re = remElement([3,2,2,3])
re.remLogic(2)
print re