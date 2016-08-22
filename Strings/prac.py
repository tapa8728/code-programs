import collections
from collections import deque

# word ladder
# 


wordList = ["hot","dot","dog","lot","log"]

beginWord = "hit"
endWord = "cog"

wordList.append(endWord)

# queue to maintain the length of the path
q = deque([  [beginWord, 1] ])  # word, length
flag =0

while q:
	word, length = q.popleft()
	if word == endWord:
		print length
		flag = 1
		break;
	else:
		for i in xrange(len(word)):
			for c in 'abcdefghijlkmnopqrstuvwxyz':
				nword = word[:i] + c + word[i+1:]
				if nword in wordList:
					wordList.remove(nword)
					q.append([ nword, length+1])
if flag == 0:
	print "Not found"
