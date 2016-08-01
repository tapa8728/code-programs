## HEAP in python

# heapq contains following methods:
# heappush(h, val)
# heappop(h)
# heappushpop(h)
# heapreplace(h)
# heapify(lis) -- needs to be done only when the root is deleted, since the whole heap gets imbalanced
# delete - particular elemnt from the list(heap) and then heapify only if the deleted element was the root


from heapq import *

class Heap(object):
    def __init__(self):
            self.heap = set() 
            
    def delete_(self, val):
        if self.heap and val in self.heap:
            self.heap.remove(val)
            heapify(self.heap)  # has a cost
        else:
            pass
    
    def insert_(self, val):
        heappush(self.heap, val)
    
    def minheap(self):
        print self.heap[0]

h = Heap()

n = 10000
# y = input()
# for each in xrange(n):
#     ip = map(int, raw_input().split())
#     if ip[0]==1:
#         h.insert_(ip[1])
#     elif ip[0]==2:
#         h.delete_(ip[1])
#     elif ip[0]==3:
#         h.minheap()
#     else:
#         pass