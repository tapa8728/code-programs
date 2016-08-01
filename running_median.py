# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
python implements minheap, but we can use _heapify_max to re-heapify the heap as a max heap. 
In case of very large inputs, using _heapify_max may be costly so we can store the elements 
in the max_heap as -ve values

Algorithm - 
We are basically putting each element into a bag(heap) and then balancing the bags so 
that the difference betwen the bags is always < 1
1. put the first element in min_heap  and return that as median(1)
   put the next element in min_heap if if its value is greater than min_heap[0](root)
    else put it in max_heap
2. **Balance the Heaps**:
    if max_heap is bigger than min_heap, remove root of max_heap and put it into min_heap
    _heapify_max(max_heap)
    if min_heapis bigger than max_heap, remove root of min_heap and put it into max_heap
    _heapify_max(max_heap)
3. Now if min_heap is bigger-
    median: min_heap[0]
   if max_heap is bigger - 
    median: max_heap[0]
if both are equal - median is the acg of the roots


'''


import heapq

minHeap = []
maxHeap = []

N = int(raw_input())
first = float(raw_input())
heapq.heappush(minHeap, first)
#print "min", minHeap
#print "max", maxHeap
print first
for i in xrange(2,N+1):
    cur = float(raw_input())
    if cur > minHeap[0]:
        heapq.heappush(minHeap, cur)
    else:
        heapq.heappush(maxHeap, cur)
        heapq._heapify_max(maxHeap)
    # Balance the heaps
    if len(maxHeap) - len(minHeap) > 1:
        maxs = heapq.heappop(maxHeap)
        heapq._heapify_max(maxHeap)
        heapq.heappush(minHeap, maxs)
    elif len(minHeap) - len(maxHeap) > 1:
        mins = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, mins)
        heapq._heapify_max(maxHeap)
    #print "min", minHeap
    #print "max", maxHeap
    if i % 2 == 1:
        if len(minHeap) > len(maxHeap):
            print minHeap[0]
        else:
            print maxHeap[0]
    else:
        print (minHeap[0] + maxHeap[0]) / 2