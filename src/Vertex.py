import Edge

class Vertex():
  def __init__(self,id):
    """
    """
    self.id = id
    self.adjacency_list = []

  def add_edge(self,edge):
    """
    """
    self.adjacency_list.append(edge)
  