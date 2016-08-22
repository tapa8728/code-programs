'''

BINARY SEARCH TREE 

1. create
2. insert node n
3. delete node n
4. find/update node n
5. print - inorder, preorder, postorder, level order
6. re-set the tree
7. Find the level of a node in the tree
8. Return depth of the tree

'''
import collections
from collections import deque

## node class 
class Node(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

## Binary seach tree class 
class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def getroot(self):
        if self.root:
            print self.root.data
        else:
            print "Tree is empty without root"

    ## Add to tree
    #--------------------------------------------
    def insert(self, val):
        if not self.root:
            self.root = Node(val) 
            print "{} added as the root of the tree".format(val)
        else: ## if root exists, recurse on the tree
            self._insert(val, self.root)

    ## -- insert recursion function
    def _insert(self, val, node):
        if val < node.data: ## insert in the left subtree:
            if node.left == None:
                node.left = Node(val)
                print "{} added as the left child of {}".format(val, node.data)
            else:
                self._insert(val, node.left)
        elif val > node.data: ## insert in the right subtree
            if node.right ==None:
                node.right = Node(val)
                print "{} added as the right child of {}".format(val, node.data)
            else:
                self._insert(val, node.right)
        else: ## if equal
            print "{} node already exists in the tree".format(val)


    ## Find 'n' in tree
    #--------------------------------------------------
    def find(self, n):
        if not self.root:
            print "Tree is empty! Nothing to be found"
        else:
            if self.root.data == n:
                print "{} found as the root of the tree".format(n)
                return True
            else: #recurse on the rest of the tree
                self._find(n, self.root)
        return False

    ## --find recursion function
    def _find(self, n, node):
        if node.data == n:
            print "{} found !!".format(n)
            return True
        elif n < node.data: ## search in the left subtree
            self._find(n, node.left)
        else:
            self._find(n, node.right)

    ## Print the tree - INORDER (expected ascending sorted array)
    #-----------------------------------------------------
    def inorder_print(self):
        if not self.root:
            print "No tree to print!"
        else:
            self._inorder(self.root)

    # -- inorder recursion function
    def _inorder(self, node):
        if not node:
            return False
        else:
            self._inorder(node.left)
            print "{}  ".format(node.data),
            self._inorder(node.right)

    ## Print the tree - PREORDER 
    def preorder_print(self):
        if not self.root:
            print "no tree to print!"
        else:
            self._preorder(self.root)

    def _preorder(self, node):
        if not node:
            return False
        else:
             print "{}".format(node.data),
             self._preorder(node.left)
             self._preorder(node.right)

    ## Print the tree - POSTORDER
    def postorder_print(self):
        if not self.root:
            print "No tree to print"
        else:
            self._postorder(self.root)

    def _postorder(self, node):
        if not node:
            return False
        else:
            self._postorder(node.left)
            self._postorder(node.right)
            print "{}".format(node.data),

    ## print the tree - LEVEL order
    def levelorder_print(self):
        if not self.root:
            print "No tree to print!"
        else:
            node = self.root
            level_q = deque([node])
            while level_q:
                n = level_q.popleft()
                print "{}  ".format(n.data), 
                if n.left:
                    level_q.append(n.left)
                if n.right:
                    level_q.append(n.right)

    ## Find level of a particular node in the tree
    def findLevel(self, n):
        if not self.root:
            print "Tree does not exist"
            return False
        else:
            level = 1 #starting at the root
            self._levelfinder(self.root, n, level)
        return False

    def _levelfinder(self, node, n, level):
        if n == node.data:
            print "\n{} found at level {}".format(n, level)
            return True
        elif n < node.data:
            self._levelfinder(node.left, n, level+1)
        elif n > node.data:
            self._levelfinder(node.right, n, level+1)

    ## Find depth of the tree
    # Return height of tree rooted at this node.

    def depth(self):
        if self.root ==None:
            print "Tree is empty!"
            return 0
        else:
            print self._depth(self.root)

    def _depth(self, node):
        if node == None:
            return 0
        if node.right == None and node.left == None:
            return 1
        else: # either left or right child is present 
            l_depth = 1 + self._depth(node.left)
            r_depth = 1 + self._depth(node.right)
        #print "left depth -", l_depth
        if l_depth > r_depth:
            return l_depth
        else:
            return r_depth

    # Lowest common ancestor - assuming n1 and n2 are in tree
    def lca(self, n1, n2):
        if not self.root:
            print "no tree!"
            return False
        else:
            node = self.root
            while node:
                if node.data > max(n1, n2):
                    node = node.left # they belong in the left subtree
                elif node.data < min(n1, n2):
                    node = node.right
                else:
                    print "LCA is {}".format(node.data)
                    return True
        return False

bst = BinarySearchTree()

bst.insert(10)
bst.insert(15)
bst.insert(8)
bst.insert(9)
bst.insert(16)
bst.insert(13)
bst.insert(5)

bst.getroot()

print "INORDER"
bst.inorder_print()

print "\nPREORDER"
bst.preorder_print()

print "\nPOSTORDER"
bst.postorder_print()

print "\nLEVEL ORDER(BFS)"
bst.levelorder_print()

bst.findLevel(16)

print "\nDepth of tree is --",
bst.depth()

print "\nLCA of 5 and 9 is"
print bst.lca(5, 9)