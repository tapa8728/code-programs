# To check if given tree is a BST or not:
## 2 methods:
### - Do inorder traversal & the array should be in ascending order -- O(n^2)
### - use recursion: root, -infinity, +infinity -- O(n)

'''
IsValidBST(root,-infinity,infinity);

bool IsValidBST(BinaryNode node, int MIN, int MAX) 
{
     if(node == null)
         return true;
     if(node.element > MIN 
         && node.element < MAX
         && IsValidBST(node.left,MIN,node.element)
         && IsValidBST(node.right,node.element,MAX))
         return true;
     else 
         return false;
}

'''

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

	######################################################
	def isBST(self):
		if self.root == None:
			print "Tree is empty"
			return None
		else:
			return self._checkBST(self.root, -float('inf'), float('inf'))

	def _checkBST(self, node, min, max):
		if node == None:
			return True
		if (node.value > min and
			node.value < max and 
			self._checkBST(node.left, min, node.value) and
			self._checkBST(node.right, node.value, max)):
			return True
		else:
			return False


t = Tree()
t.add(10)
t.add(9)
t.add(12)
t.add(1)
t.add(31)
if t.isBST():
	print "Valid BST"
else:
	print "Not valid BST"