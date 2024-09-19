from Vertex import Vertex
from Edge import Edge 

class DG():
    def __init__(self):
      """
      Initializes a directed graph.
      """
      self.vertices = {}

    def add_vertex(self, id):
      """
      Adds a vertex to the graph.
      """
      if id not in self.vertices:
          self.vertices[id] = Vertex(id)
    
    def add_edge(self, vertex1_id, vertex2_id, weight=0):
      """
      Adds a directed edge from vertex1 to vertex2.
      """
      if vertex1_id in self.vertices and vertex2_id in self.vertices:
          vertex1 = self.vertices[vertex1_id]
          vertex2 = self.vertices[vertex2_id]
          edge = Edge(vertex1, vertex2, weight)
          vertex1.add_edge(edge)

    def display_graph(self):
      """
      Displays the graph.
      """
      for vertex in self.vertices.values():
          print(f"{vertex.id}: {[str(edge) for edge in vertex.adjacency_list]}")


class UG():
    def __init__(self):
        """
        Initializes an undirected graph.
        """
        self.vertices = {}

    def add_vertex(self, id):
        """
        Adds a vertex to the graph.
        """
        if id not in self.vertices:
            self.vertices[id] = Vertex(id)
      
    def add_edge(self, vertex1_id, vertex2_id, weight=0):
        """
        Adds an undirected edge between vertex1 and vertex2.
        """
        if vertex1_id in self.vertices and vertex2_id in self.vertices:
            vertex1 = self.vertices[vertex1_id]
            vertex2 = self.vertices[vertex2_id]
            edge = Edge(vertex1, vertex2, weight)
            vertex1.add_edge(edge)
            vertex2.add_edge(edge)

    def display_graph(self):
        """
        Displays the graph.
        """
        for vertex in self.vertices.values():
          print(f"{vertex.id}: {[str(edge) for edge in vertex.adjacency_list]}")


dg = DG()

vertices = [0, 1, 2, 3, 4, 5]
for v in vertices:
    dg.add_vertex(v)

edges = [(0, 4), (0, 5), (1, 2), (1, 3), (2, 1), (2, 3), (2, 5), (3, 1), (3, 4), (4, 2), (4, 0), (5, 3), (5, 4)]
for edge in edges:
    dg.add_edge(edge[0], edge[1])

dg.display_graph()
