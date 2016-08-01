
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s) +1)
        dp[0] = True
        for i in xrange(len(s)): # 8
            for j in xrange(i, -1, -1): #start, stop, skip: from i ... 0
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[len(s)]
        
s = Solution()
print s.wordBreak("leetcode", ["leet","code"])              