'''

How many chars do we have to remove at minimum to convert

S= "acdbfda" to a palindrome

DYNAMIC PROGRAMMING 
if s[i] == s[j]  then dp[i][j] = dp[i+1][j-1]
				 (do nothing, no cost of operations)

else s[i] != s[j] then dp[i][j] = min( dp[i+1][j], dp[i][j-1] ) + 1
				(drop the first/last char -- whichever is the cheapest -- minimum)

'''

s = "aba"

# initialize all to zero
dp = [[ int(0) for i in range(len(s)+1)]  for i in range(len(s)+1)	] 

for each in dp:
	print each


def ispalindrome(m):
	return m[:] == m[::-1]

for i in range(0, len(s)):
	for j in range(0, len(s)):
		if s[i]  ==  s[j]:
			dp[i][j] = dp[i+1][j-1]
		elif s[i] != s[j]:
			dp[i][j] = min( dp[i+1][j], dp[i][j-1] ) + 1
	for each in dp:
		print each
	print "--------------"


	

print dp[0][len(s)]	