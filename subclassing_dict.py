from UserDict import UserDict
class DD2(UserDict):

	def __init__(self,dic):
		self.data = dic

	def __getitem__(self,key):
		if key not in self.data:
			self.__missing__(key)
			return key
		else:
			return self.data[key]

	def __missing__(self,key):
		return key


d= {'a':10,'b':20}
a = DD2(d)

print a['c']