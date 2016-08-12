#depth first search 
# Using adj. matrix to store the graph, so have to go through each element 
# Time complexity: O(n^2)

# adj. matrix for dense graphs A,B,C
G = [[0,1,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,1,1],[0,0,1,0,0,0],[0,0,1,1,1,1], [0,0,1,0,1,0]]
# list of vertices
vx = range(len(G))

# visited dictionary - set all to false
visited = {}
for each in vx:
	visited[each] = False


def explore(G, root):
	visited[root] = True
	print "visited :: {}".format(root)
	for each in vx:
		if not visited[each] :  # instead of using visited[each] == False
			if G[root][each]!=0:
				explore(G, each)		# recurse

start = 2
explore(G, start)
k  =[each  for each in visited if visited[each]==True ]
print "Nodes reachable from {} are: {}".format(start,k)
print visited