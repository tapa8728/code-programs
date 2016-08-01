# Enter your code here. Read input from STDIN. Print output to STDOUT


from itertools import *
import math

class MaxIt(object):
    def __init__(self):
        self.firstIp = raw_input().split()
        self.K, self.M = int(self.firstIp[0]), int(self.firstIp[1])
        self.master = [] #list of the next K lists
        for each in range(self.K):
            self.master.append(map(int, raw_input().split()))
        #print self.master
        self.maxList()
    
    def maxList(self):
        self.maxLis = [max(each)     for each in self.master]
        #print self.maxLis
        self.maxFormula()
    
    def maxFormula(self):
        self.result = 0
        for each in self.maxLis:
            self.result+=math.pow(each, 2)
        print int((self.result)%self.M)

oneMax = MaxIt()

        '''
        # Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

def res(a, m):
    return sum([x * x for x in a]) % m
[k, m] = [int(x) for x in raw_input().split()]
list_k = []
for i in range(k):
    a = [int(x) for x in raw_input().split()]
    a.pop(0)
    list_k.append(a)

ans = 0
for x in itertools.product(*list_k):
    ans = max(ans, res(x,m))
print ans
     
    
        '''