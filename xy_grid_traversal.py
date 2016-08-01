
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Solution - 
d d r r r r r r
d r d r r r r r  ...

8c2 or 8c6

'''


import math
from math import *

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        down = m-1
        rights = n-1
        z = down +rights
        
        # C( down + rights, rights)
        f = factorial
        return f(z)/f(z-down)/f(down)