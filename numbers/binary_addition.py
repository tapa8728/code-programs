'''
BINARY ADDITION

"{0:b}".format(100) # bin: 1100100
"{0:x}".format(100) # hex: 64
"{0:o}".format(100) # oct: 144

using int(a, 2) is a faster way than using eval. Eval() is very slow

>>> from timeit import timeit
>>> timeit("int('1010101010101010', 2)")
0.82430828797186
>>> timeit("eval('0b1010101010101010')")
15.573771070163502

'''

class Solution:
    def addBinary(self, a, b):
        sum = bin(eval('0b' + a) + eval('0b' + b))
        return sum[2:].zfill(8)   # zfill is used to fill up the zeroes in the front

s = Solution()
print s.addBinary("110", "11100")