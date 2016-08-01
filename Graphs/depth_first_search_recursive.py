'''
	DEPTH FIRST SEARCH
	For undirected Graphs

	Classes - 

		Vertex:
		-------
		name, neighbors =[], discovery, finish, color (black = unfinished, blue = finished)

		Graph:
		------
		vertices = {} # vx_name : Vertex object

	We can build the graph by providing a list of edges. 

	Recursive approach 

'''
import collections
from collections import *

class Vertex(object):
	def __init__(self, n): 
		self.name = n
		self.neighbors = list() #each vx will have a list of neighbors eg: [A, C, D, M]
		self.discovery = 0
		self.finish = 0
		
	def add_neighbor(self, neigh):
		if neigh not in self.neighbors:
			self.neighbors.append(neigh)
			self.neighbors.sort() # keep the list sorted

class Graph(object):
	vertices = {} #dic to maintain the vertices in the graph {vx.name : Vertex obj}
	time = 0 
	visited = list() # to maintain list of visited nodes

	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " 
						+ str(self.vertices[key].discovery) + "/" 
						+ str(self.vertices[key].finish) + "--"
						+ str(self.vertices[key].color))

	## Add a vertex to the graph:
	#  Check if vx is an object of type "Vertex"
	#  vx is not already in graph
	def add_vertex(self, vx):
		if isinstance(vx, Vertex) and vx.name not in self.vertices:
			self.vertices[vx.name] = vx
			return True
		else:
			return False

	## Add an endge between two vertices in the Graph:
	#  check if u, v are both in graph
	#  Add u as neighbor of v and v as neighbor of u
	def add_edge(self, u, v): # to add an edge from u to v
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False

	def dfs(self, startVx):
		global time
		time = 1
		self._dfs(startVx)


	def _dfs(self, vx):
		global time
		self.visited.append(vx.name)
		vx.discovery = time
		time = time + 1
		for v in vx.neighbors:
			if self.vertices[v].name not in self.visited:  # black means unvisited
				self._dfs(self.vertices[v]) # explore it 
		vx.finish = time
		time = time + 1
		
g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

# automate the adding of vertex
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i))) # add vertices from A --> J

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.dfs(a)
g.print_graph()

print "DFS order - ", g.visited


	