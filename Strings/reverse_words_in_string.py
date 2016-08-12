''' 
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".


'''

s = "the    sky is blue"


m = s.split()  # this takes care of trimming
# for each in m:
# 	if each == "":
# 		m.remove(each) 
m.reverse()
print " ".join(m)

#print " ".join(s.split()[::-1])