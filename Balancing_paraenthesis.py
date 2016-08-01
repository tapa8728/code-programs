
# Try to check if the given input string has balanced paranthesis or not
## INPUT:
##  []}
##  [{}
##  {([
##  ]}

import sys

iparens = iter('{}()<>[]')
parens = dict(zip(iparens,iparens))
opening = parens.keys()
closing = parens.values()
stack = []

t = int(raw_input().strip())
for each in xrange(t):
    flag = 0      # reset the flag
    stack = []    # clear the stack
    s = raw_input().strip()
    for c in s:
        if c in opening:
            stack.append(c)
        elif c in closing:
            if stack: #if stack is not empty
                top = stack.pop()
                if parens[top] == c:
                    pass
                else:
                    flag = 1
                    break
            else:   # trying to pop from an empty stack
                flag =1
                
    if flag == 0 and len(stack)==0: #stack should be empty
        print "YES"
    else:
        print "NO"
   
   