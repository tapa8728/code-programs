from bitarray import bitarray
import mmh3

filter = bitarray(10)
filter.setall(0)

b1 = mmh3.hash("tipsy", 41)%10
print "tipsy hashed to -", b1
filter[b1] = 1

b2 = mmh3.hash("reema", 43) % 10
print "reema hashed to -", b2
filter[b2] = 1

## filter contains - tipsy, reema
print "FILTER -- ", filter    

## lookup
l1 = mmh3.hash("tipsy", 41) % 10 #Equals 0
print "Tipsy lookup hash -", l1
l2 = mmh3.hash("boo", 43) % 10 #Equals 4
print "boo lookup hash - ", l2


## can be put into a look-up function
if filter[l1] == 1:
    print "Tipsy Probably in set"
else:
    print "Tipsy Definitely not in set"

if filter[l2] == 1:
    print "boo Probably in set"
else:
    print "boo Definitely not in set"
