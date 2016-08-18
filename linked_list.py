'''
LINKED LIST

Functions - 
1. Insert
2. Size
3. Search
4. Delete

'''

class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None 			#set to none

class LinkedList(object):
	def __init__(self):
		self.head = None

	def printList(self):
		curr = self.head
		print "[ ",
		while curr:
			print str(curr.data), 
			curr = curr.next
		print " ]"

    ## 'val' - value to be inserted
    ## always insert at the beginning 
	def insert(self, val):
		newNode = Node(val)
		newNode.next = self.head
		self.head = newNode

	## Size of the linkedlist
	def size(self):
		if not self.head:
			return 0
		else:
			curr = self.head
			count = 0
			while curr:
				count = count + 1
				curr = curr.next
			return count

	## search - traverse throught the linkedlist and return if 'val' matches to the data
	def search(self, val):
		curr = self.head
		while curr:
			if curr.data == val:
				return True
			else:
				curr = curr.next
		return False


	## delete - maintain a previous pointer for "frog leaping"
	def delete(self, val):
		prev = None
		curr = self.head
		while curr:
			if curr.data == val:
				if not prev: 	## head contains the data we want to Delete
					self.head = curr.next
					curr.next = None 
					return True
				else: 			## deleting from the center of the list
					prev.next = curr.next
					curr.next = None
					return True
			else:
				prev = curr
				curr = curr.next
		return False

	## Completely clear the LL
	def clear(self):
		self.__init__()


## MAIN function
if __name__ == '__main__':
	lis = LinkedList()
	lis.printList()
	lis.insert(6)
	lis.printList()
	print "size -- ", lis.size()
	raw_input()
	lis.insert(3)
	lis.insert(4)
	lis.printList()	
	print "size -- ", lis.size()
	if lis.delete(9): 
		print "9 deleted"
	else:
		print "9 not found"
	lis.printList()
	if lis.delete(3): 
		print "3 deleted"
	else:
		print "3 not found"
	lis.printList()
	print "lets clear out now .."
	lis.clear()
	lis.printList()
