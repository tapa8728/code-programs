a = [2,0,1,5]

temp = 0
for i, v in enumerate(a):
	for j in range(1,i):
		if a[j-1] > a[j]: # now swap
			temp = a[j]
			a[j] = a[j-1]
			a[j-1] = temp

print "after sorting -", a