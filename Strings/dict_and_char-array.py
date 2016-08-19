'''Given a dictionary of strings, and a char array.

Find all entries in the dictionary in which all the strings chars can be found in the char array 

Ex: char = ['a', 'b', 'm', 't', 'l', 'e', 'c']
	dic = {"battle", "cattle", "men", "cow", "mmmmm", "hmmmm"}
'''

import collections

char = ['a', 'b', 'm', 't', 'l', 'e', 'c']
dic = {"battle", "cattle", "men", "cow", "mmmmm", "hmmmm"}

charset = set(char)

dicset = [set(list(each)) for each in dic]

fulldic = zip(dic, dicset) #list of tuples

#list of strings whose all chars can be found in the char array
result = [] 

for each in fulldic:
	if each[1] <= charset:  #intersection operation
		result.append(each[0])

print "Dictionary - {}".format(dic)
print "Char array - {}".format(char)
print "Result = {}".format(result)