
class Node(object):
    def __init__(self, val):
        self.l = None   #left pointer
        self.r = None   #right pointer
        self.v = val

class Tree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)       #start from the root node

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):     # left subtree
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else: # val > node.v
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)         # recurse on the left subtree
        elif(val > node.v and node.r != None):
            self._find(val, node.r)         # recurse on the right subtree

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print "is this printing?"
print (tree.find(3)).v

print "is this printing?"
print tree.find(10)
tree.deleteTree()
tree.printTree()