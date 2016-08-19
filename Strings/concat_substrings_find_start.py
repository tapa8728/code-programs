'''
You are given a string, s, and a list of words, words, that are all of the same length. 
Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once 
and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str  # "aaa"
        :type words: List[str] "a", "a"
        :rtype: List[int]
        """
        k = [''.join(x) for x in list(permutations(words))] #substrings
        print "substrings - {}".format(k)
        start = []
        for each in k:
            start += [m.start() for m in re.finditer(each,s)] 
            
               
        print start         
        m= list(set(start))
        
        return m

# ------------------------------------------------

import itertools
import re
from itertools import *

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str  # "aaa"
        :type words: List[str] "a", "a"
        :rtype: List[int]
        """
        k = [''.join(x) for x in list(permutations(words))] #substrings
        #print "substrings - {}".format(k)
        start = []
        l = len(k[0]) #size of substrings will never change
        for i in range(len(s)):
            for each in k:
                if each == s[i:i+l]:
                    start.append(i)
            
        print start         
        m= list(set(start))
        
        return m