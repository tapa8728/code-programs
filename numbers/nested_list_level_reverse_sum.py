'''

RECURSION - 


[1, [2,3], [ [4] ]]


level number :
1*1 + 2*(2+3) + 3*(4) = 23

reverse level number :
3*1 + 2*(2+3) + 1*(4) = 3 +10 +4 = 17
-     -         -


'''

k = [1, [2,3], [ [4]]]

level = 0	# nestedness


nestedflag = True # does it contain anymore nested lists in it ?
res = list()  

depth = []

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
	depth.append(lev)
	print "RES is ---", res, "WHEN K is --", k
	

levelList(k, 0)
print res
summ = 0
print "Depth - ", depth
lvl = max(depth)
print "max depth is --", lvl
for each in res:
	summ += each[0]*(lvl+1 - each[1])  # adding one because we start with 1

print summ