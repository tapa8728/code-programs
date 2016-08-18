'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37 
1 < 1.0.0.1

hint: play on the length of the version numbers
'''

class version(object):

	def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split(".")) # 1.2.2
        v2 = map(int, version2.split(".")) # 1.2
        
        n = max(len(v1), len(v2))
        
        for i in range(n):
            if i < len(v1): # current iteration exists in v1.
                n1 = v1[i]
            else:
                n1 = 0
                
            if i < len(v2): # current iteration exists in v2
                n2 = v2[i]
            else:
                n2 = 0
                
            if n1 > n2: return 1
            elif n1 < n2: return -1
            else: pass
        
        return 0


v = version()
print v.compareVersion("1.1", "0.0.0.1")


