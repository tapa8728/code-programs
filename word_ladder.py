'''
WORD LADDER

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''
import collections



class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.append(endWord)
        queue = collections.deque([[beginWord, 1]])
        print "QUEUE initially -- {}".format(queue)
        while queue:
            print "QUEUE is --{}".format(queue)
            print "WORDLIST is --{}".format(wordList)
            word, length = queue.popleft()
            print "Popped Queue --  {},{}".format(word, length)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]   #change each letter of the start word sequentially - hit, sit, bit, cit ...
                    print "pass {} -- next word -- {} ".format(i, next_word)
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
                        print "Updated -- QUEUE is --{}".format(queue)
                        print "Updated -- WORDLIST is --{}".format(wordList)
                    raw_input()
        return 0


s = Solution()
print s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])