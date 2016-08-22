'''

edit distance

given string S and T, check if they are both one edit distance apart 

'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
                
        ##  [[int(0)]*len(word1)]*len(word2)
        ## Set all to zero
        ED = [[int(0) for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        
        ## set the top row
        for each in xrange(len(word1)+1):
            ED[each][0] = each

        ## set the first column
        for each in xrange(len(word2)+1):
            ED[0][each] = each
        
        ## loop thru each one
        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    ED[i][j] = ED[i-1][j-1]
                else: # not equal
                    ED[i][j] = min(ED[i-1][j], ED[i][j-1], ED[i-1][j-1])+1
        
        return ED[-1][-1]



s = Solution()
print s.minDistance("reemz", "reema")