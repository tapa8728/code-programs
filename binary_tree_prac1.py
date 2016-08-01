# Binary Search tree implemented 
# -- Insert
# -- Find
# -- Delete Tree

class Node(object):
	def __init__(self, val):	#wll be called when a new node is initialized
		self.left = None
		self.right = None
		self.value = val

class Tree(object):
	def __init__(self):			# when the tree is initialized, it will not have a root node 
		self.root = None 		# root is the class variable of Tree

	def getroot(self):
		return self.root

	## --------- ADD A NODE -------------- ##
	def add(self, val):
		if (self.root == None):		# if the tree is empty, make the first addition as the root
			self.root = Node(val)
			print "Node with val {} added as root".format(val)
		else:
			self._add(val, self.root) 

	def _add(self, val, node):
		# is value less than root-val(LEFT)
		if val < node.value:
			if node.left != None: #left subtree exists
				self._add(val, node.left) #recurse on the left subtree
			else:
				node.left = Node(val)
				print "node with value {} added to left ".format(val)
		# is value greater than root-val (RIGHT)
		else:
			if node.right != None: #right subtree exists
				self._add(val, node.right)
			else:
				node.right = Node(val)
				print "node with value {} added to right ".format(val)

	## --------- FIND A NODE -------------- ##
	def find(self, val):
		if self.root == None:
			return None
		else:
			self._find(val, self.root)

	def _find(self, val, node):
		if (node.value==val):
			print "Value {} found".format(val)
		elif (val < node.value and node.left!=None):
			self._find(val, node.left)
		elif (val > node.value and node.right!=None):
			self._find(val, node.right)
		else:
			print "Value {} not found :(".format(val)

	## --------- DELETE WHOLE TREE -------------- ##
	def deletetree(self):
		if self.root == None:
			return None
		else:
			self.root = None #garbage collector will take care of this. 

	## --------- PRINT THE TREE -------------- ##
	def printTree(self):
		if self.root!=None:
			self._printTree(self.root)
		else:
			print "Tree is empty!!"

	def  _printTree(self, node):
		if node==None:
			return None
		else:
			self._printTree(node.left)
			print str(node.value) + " ", 
			self._printTree(node.right)

t1 = Tree()
t1.add(4)
t1.add(5)
t1.add(6)
t1.add(10)
t1.add(2)
print (t1.getroot()).value
print "Lets find stuff"
print t1.find(41)
print t1.find(4)
t1.printTree()
t1.deletetree()
t1.printTree()
