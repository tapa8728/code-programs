''' 
Inverting a BST :

		BST 						Inverted BST

		4								4
	2		7		--->			7		2
  1   3   6   9					  9   6   3   1

inorder:							inorder:
---------							----------
1 2 3 4 6 7 9						9 7 6 4 3 2 1
(ascending order)                   (descending order)

Solution: 
1) Get the inorder traversal of the BST, re-create the BST by adding larger values to left and smaller to the right
2) Use BFS iteratively and swap the left and right children. Notice that the root is constant in both cases

'''
class Node(object):
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

class Tree(object):
	def __init__(self):
		self.root = None

	## ADD
	def insert(self, val):
		if self.root == None:
			self.root = Node(val)
			print "{} added as the root".format(self.root.value)
		else:
			self._insert(self.root, val)

	def _insert(self, node, val):
		if val > node.value: #add tot he right subtree
			if node.right==None:
				node.right = Node(val)
				print "{} added to the right of {}".format(val, node.value)
			else: #recurse on the right subtree
				self._insert(node.right, val)
		elif val < node.value:
			if node.left==None:
				node.left = Node(val)
				print "{} added to the left of {}".format(val, node.value)
			else: #recurse on the left subtree
				self._insert(node.left, val)
		elif node.value == val:
			print "{} is Duplicate to {}".format(val, node.value)

	## PRint
	def printTree(self):
		if self.root == None:
			print "No tree!"
		else:
			self._inorder(self.root)

	def _inorder(self, node):
		if node == None:
			return False
		else:
			self._inorder(node.left)
			print "{} ".format(node.value),
			self._inorder(node.right)

	## Recursive Inverse
	def invert(self):
		if self.root==None:
			return "No trrree to invert"
		else:
			print "Let's Invert"
			self._invert(self.root)

	def _invert(self, node):
		if node:
			node.left, node.right = self._invert(node.right), self._invert(node.left)
			return node
	
	## Iterative Inverse
	def invert2(self):
		print "lets try iterative inverts"
		stack = [self.root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack.append(node.left)
				stack.append(node.right)
		



t = Tree()
t.insert(4)
t.insert(2)
t.insert(7)
t.insert(1)
t.insert(3)
t.insert(6)
t.insert(9)
t.printTree()
t.invert2()
t.printTree()
