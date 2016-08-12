'''
DFS iterative using stack. 


'''
import collections
from collections import *

class Vertex(object):
	def __init__(self, n):
		self.name = n
		self.neighbors = list() # why not list??


class Graph(object):
	vertices = defaultdict(list)
	stack = []
	visited = []

	def add_vertex(self, v):
		if isinstance(v, Vertex) and v not in self.vertices:
			self.vertices[v.name] = v.neighbors

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].append(v)
			self.vertices[v].append(u)

	def dfs(self, startvx):
		print self.vertices
		self.stack.append(startvx.name)
		while self.stack: # while stack exists
			top = self.stack.pop() 			# pop from stack
			self.visited.append(top)		# mark visited
			# Process_early stub here(for start time)
			for each in self.vertices[top]:
				if each not in self.visited:
					# Process_edge stub here
					self.stack.append(each)
			# Process_late stub here

g = Graph()
a = Vertex('A')
# automate the adding of vertex
for i in range(ord('A'), ord('D')):
	g.add_vertex(Vertex(chr(i))) # add vertices from A --> J

# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
edges = ['AB', 'BC', 'AC']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.dfs(a)
#g.print_graph()

print "DFS order - ", g.visited