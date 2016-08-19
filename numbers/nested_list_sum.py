'''

RECURSION - 


[1, [2,3], [6, [4] ]]


'''

k = [1, [2,3], [ [4]]]

level = 0	# nestedness


nestedflag = True # does it contain anymore nested lists in it ?
res = list()  

def levelList(k, lev):
	
	s = 0	# sum
	lev = lev +1
	print " WHEN K is --", k , "lev is - ", lev
	for each in k:
		if isinstance(each, list):
			levelList(each, lev)
		else: 
			s = s + each
	res.append([s,lev]) ## append the level# and the sum to stack as a tuple
	print "RES is ---", res, "WHEN K is --", k
	

levelList(k, 0)
print res
summ = 0
for each in res:
	summ += each[0]* each[1]

print summ