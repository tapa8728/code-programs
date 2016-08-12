'''
BREADTH FIRST SEARCH 

A BFS-tree gives us the shortest path from the starting vertex to every other vertex 
in the graph. 
This path is obtained by storing the parent of every node and then reversing the parents

Also called level-order traversal
Data structure used: Queue

Applications:
Count the connected components
2-color vertex graph problem
shortest path problem (only if no-weight)

'''
import collections
from collections import *
import Queue
from Queue import *

class Vertex(object):
	def __init__(self, v_name):
		self.name = v_name
		self.neighbors = list()

class Graph(object):
	vertices = defaultdict(list)  # bunch of vertex objects
	visited = []
	parent = {} 
	q = Queue()

	def add_vertex(self, v):
		if isinstance(v, Vertex) and v not in self.vertices:
			self.vertices[v.name] = v.neighbors 

	def add_edge(self, u, v): # Passing u.name, v.name
		if u in self.vertices and v in self.vertices:
			self.vertices[u].append(v)
			self.vertices[v].append(u)

	def BFS(self, start):  #start.name
		self.q.put(start)
		while not self.q.empty():
			vx = self.q.get() 
			if vx not in self.visited:
				self.visited.append(vx)
			# Process_early stub here
			for adj_v in self.vertices[vx]:
				if adj_v not in self.visited:
					# Process_adjacent_edges stub here
					self.parent[adj_v] = vx
					self.visited.append(adj_v)
					self.q.put(adj_v)
				else: 
					pass
			# Process_late stub here
			
g = Graph()



## add vertices
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i))) 

## add edges
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for e in edges:
	g.add_edge(e[1:], e[:1])


g.BFS('A')  #entering only the name of the vertex. 

print "BFS ordering - ", g.visited
print "BFS Parents - ", g.parent