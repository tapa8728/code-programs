lis = ['cat', 'banana', 'dog', 'nana', 'walk', 'catcatcatcatcatcat','walker', 'dogwalker', 'catdogwalkerbanana', 'dogdogwalkercatcat']
dic={}
for each in lis:
	dic[each]={}

for full in lis:
	for sub in lis:
		if len(sub) > len(full): #'banana' in 'cat'
			pass
		elif sub==full: #'cat' in 'cat'
			pass
		elif full.count(sub) > 0:
			dic[full][sub] = 1
			
print dic
print "Most occurences is {}".format(sorted(dic, key=lambda x: (len(dic[x])), reverse=True)[0])

#'dogwalker':{'dog':1, 'walk':1, 'walker':1}, 'cat'

