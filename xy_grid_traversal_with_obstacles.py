'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

'''


class Solution:
# @param obstacleGrid, a list of lists of integers
# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		#print "obstacleGrid {}".format(obstacleGrid)
	    m = len(obstacleGrid)
	    n = len(obstacleGrid[0])
	    print "obstacleGrid {}".format(obstacleGrid)
	    print ""
	    ResGrid = [[0 for x in range(n+1)] for x in range(m+1)]
	    print "Resgrid 1 {}".format(ResGrid)
	    ResGrid[0][1] = 1
	    print "Resgrid 2 {}".format(ResGrid)
	    for i in range(1, m+1):
	        for j in range(1, n+1):
	            if obstacleGrid[i-1][j-1] == 0:
	                ResGrid[i][j] = ResGrid[i][j-1]+ResGrid[i-1][j]
	                print "i::{} and j::{}".format(i,j)
	                print "Resgrid -- {}".format(ResGrid) 

	    return ResGrid[m][n]


s = Solution()
print s.uniquePathsWithObstacles([  [0,0,0],  [0,1,0],  [0,0,0]])