'''
You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2
Sample Output

0.8333
--------------------------------------------------------------------------
Explanation

All possible unordered tuples of length 2 comprising of indices from 1 to 4  are:
(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)

Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter 'a'.

Hence, the answer is 5/6 = 0.833 .
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
class LevelUp(object):
    def __init__(self):
        self.num = input()
        self.ipList = raw_input().split()
        self.indice = input()
        self.k = []
        self.probOfA, self.totalProb = 0, 0
   
    def indiceComb(self):
        for each in combinations( xrange(1,self.num+1), self.indice):
            self.k.append(each)
       # print self.k
        self.totalProb = len(self.k)
        self.probCalc()
    
    def probCalc(self):
        for each in self.k: #(1,2,3,4)
            for i in range(len(each)): 
                if self.ipList[each[i]-1] == 'a':
                    self.probOfA+=1
                    break
                else:
                    pass
                
        print float(self.probOfA)/float(self.totalProb)        
        
levelOne = LevelUp()
levelOne.indiceComb()