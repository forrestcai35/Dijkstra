

class Edge():
    def __init__(self, vertex1, vertex2, weight=0):
        """
        Initializes an Edge object with source and destination vertices and an optional weight.
        """
        self.src = vertex1
        self.dest = vertex2
        self.weight = weight

    def __str__(self):
        return f"({self.src.id} -> {self.dest.id}, weight={self.weight})"

    def __repr__(self):
        return self.__str__()
