# Create a list of lists of nodes at each level of depth

import random

class Node(object):
	def __init__(self,val):
		self.left = None
		self.right = None
		self.value = val

class Tree(object):
	def __init__(self):
		self.root = None
		self.lis = []

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

	def depth(self):
		if self.root ==None:
			print "Tree is empty!"
			return 0
		else
			self._depth(self.root)

	def _depth(self, node):
		if node == None:
			return 0
		if node.right == None and node.left == None:
			return 1
		else: # either left or right child is present 
			l_depth = 1 + self._depth(node.left)
			r_depth = 1 + self._depth(node.right)
		if l_depth > r_depth:
			return l_depth
		else:
			return r_depth

	def printTree(self):
		if self.root == None:
			print "TRee is empty!"
		else:
			self._printTree(self.root)

	# pre - order traversal
	def _printTree(self, node, lis):
		if node!= None:
			print "{}--".format(node.value),
			self._printTree(node.left)
			self._printTree(node.right)