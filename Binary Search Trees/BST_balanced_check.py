'''#  To check if the given BST is balanced or not 
## A balanced BST is the one where the height of the left Subtree
## and height of the right Subtree cannot differ by more than one.
## ----------------------------------------------------------- 
# Algo-
## 1. Start at the root
## 2. calculate height of the left subtree - leftH
## 3. calculate height of the right subtree - rightH
## 4. if abs(leftH - rightH)>1:
##		False
##	  else
##      True

## Complexity - O(n) '''

class Node(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

class Tree(object):
	def __init__(self):
		self.root = None
		self.left_h=0
		self.right_h=0

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
			print "Node with value {} added as root".format(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val< node.value: #left side
			if node.left !=None:
				self._add(val, node.left)
			else:
				node.left = Node(val)
				print "Node with value {} added to the left of {}".format(val, node.value)
		else: #to the right side
			if node.right != None:
				self._add(val, node.right)
			else:
				node.right = Node(val)
				print "Node with value {} added to the right of {}".format(val, node.value)

	def isBalanced(self):
		return self.isBalancedInt(self.root)>=0

	# the left, right values of a node are returned to the left, right of its parent node..
	# do this for every node starting from the left-most node
	def isBalancedInt(self, root):
		# if tree is empty
		if root == None:
			return 0;

		left = self.isBalancedInt(root.left)
		if left<0:
			return -1
		print "left :: {} when root.val is {}".format(left, root.value)

		right = self.isBalancedInt(root.right)
		if right<0:
			return -1
		print "right :: {} when root.val is {}".format(left, root.value)
		if abs(left-right)>1:
		    return -1
		else:
			print "it comes here when {}".format(root.value)
			print "========================================="
			return max(left,right)+1 # height of root node


'''
		6
	3		7
  1  4	   -  8
  			 -  10
'''


t = Tree()
t.add(6)
t.add(3)
t.add(7)
t.add(1)
t.add(4)
t.add(8)
t.add(10)
print "is it balanced? ",t.isBalanced()