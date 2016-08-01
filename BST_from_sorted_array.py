# if sorted input array is given, crete a minimal heighted BST from it

import random

class Node(object):
	def __init__(self,val):
		self.left = None
		self.right = None
		self.value = val

class Tree(object):
	def __init__(self):
		self.root = None

	def getroot(self):
		if self.root != None:
			return self.root
		else:
			return None

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
			print "Node with value {} has been added as root".format(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node): #lesser values than root to the left always
		if val == node.value:
			return None
		if val < node.value: #left subtree
			if node.left != None:
				self._add(val, node.left)
			else:
				node.left = Node(val)
				print "Node with value {} has been added to the left of {}".format(val, node.value)
		else:   #Right subtree
			if node.right != None:
				self._add(val, node.right)
			else:
				node.right = Node(val)
				print "Node with value {} has been added to the right of {}".format(val, node.value)

	def printTree(self):
		if self.root == None:
			print "TRee is empty!"
		else:
			self._printTree(self.root)

	# inorder traversal
	def _printTree(self, node):
		if node!= None:
			self._printTree(node.left)
			print "{}--".format(node.value),
			self._printTree(node.right)

t = Tree()
a = sorted([int((random.random())*100) for each in range(10)   ], reverse=False)
print a
print "-----------------------------------------"
t.add(a[len(a)/2])
for each in a:
	t.add(each)

t.printTree()