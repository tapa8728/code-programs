s = raw_input()

# number of occurences of a substring in a given string
def occ(sub):
    ct = 0
    le = len(sub)
    for i in range(len(s)):
        if s[i:i+le] == sub:
            ct+=1
    return ct
        

#get all the contiguous substrings
lis=[s]
length = len(s)
for i in range(length):
    for j in range(i, length):
        m = s[i:j+1]
        if m!='' and m not in lis:
            lis.append(m)
         
#count number of consonant string and vowel strings
vcount, count = 0, 0
dic ={}
for each in lis:
    dic[each] = occ(each)
    
for k,v in dic.iteritems():
    if k[0] in ['A', 'E', 'I', 'O', 'U']:
        vcount+=v
    else:
        count+=v

if vcount > count:
    print "Kevin {}".format(vcount)
elif count > vcount:
    print "Stuart {}".format(count)
else:
    print "Draw"