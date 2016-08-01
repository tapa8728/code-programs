

N = 7
hist = [6, 2, 5, 4, 5, 1, 7]

# N = 5 # number of bars
# hist = [1,2,3,4,5] #list of heights of all bars in question


print hist 

stack = []
top = -1
max_area = 0
# Lets traverse through each bar now
idx = 0


while (idx < N):
    
    if len(stack) == 0 or hist[idx] >= hist[stack[top]]:
        print "{} is greater ".format(hist[idx])
        stack.append(idx)
        idx = idx +1
        print "------------------------------------------"
    else:
        # bar is lesser than top of stack
        print "{} is lesser than {} so pop {}".format(hist[idx],hist[stack[top]], hist[stack[top]])
        ht = stack.pop()
        depth = idx
        print "Depth BEFORE checking if stack exists -- {}".format(depth)
        if len(stack) > 0: # bars still exist to the left of the popped bar
            depth = idx - stack[top] - 1
            print "Depth AFTR checking that stack exists -- {}".format(depth)
        print "HEIGHT OF BAR - {}".format(hist[ht])
        area = hist[ht] * depth
        print "AREA - {}".format(area)
        max_area = max(area, max_area)
        print "MAX AREA - {}".format(max_area)
        print "------------------------------------------"
    print "Pass : {} Stack-- {}".format(idx, stack)

print "########## loop 2 #######################"
while len(stack)!=0:
    print "STACK - {}".format(stack)
    ht = stack.pop()
    depth = idx
    print "Depth = idx -- {}".format(depth)    
    if len(stack) > 0: # bars still exist to the left of the popped bar
        depth = idx - stack[top] - 1
        print "Depth AFTR checking that stack exists -- {}".format(depth)
    print "HEIGHT OF BAR - {}".format(hist[ht])
    area = hist[ht] * depth
    print "AREA - {}".format(area)
    max_area = max(area, max_area)
    print "MAX AREA - {}".format(max_area)
    print "............................................."

print "FINAL max area --{}".format(max_area)