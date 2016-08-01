from itertools import *

for i in chain(["ABC", "DEF"]):
	for e in i:
	    yield e

