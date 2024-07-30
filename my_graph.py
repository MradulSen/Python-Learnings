import pprint

class Vertex:
    def __init__ (self, name):
            self.name = name
            self.connections = []

    def add_egde(self,obj):
        self.connections.append(obj)

class Egde:
    def __init__ (self):
           self.connections = [] 

    def add_egde(self,from_ver,to_ver):
         self.connections.append(from_ver.name)
         self.connections.append(to_ver.name)

class Graph:
        def __init__(self):
            self.graph ={}

        def add_vertices(self,obj):
         self.graph.update({obj.name:obj.connections})

v1 = Vertex("1")
v2 = Vertex("2")
v3 = Vertex("3")
v4 = Vertex("4")   


e1 = Egde()
e1.add_egde(v1,v2)

e2 = Egde()
e2.add_egde(v1,v3)

e3 = Egde()
e3.add_egde(v2,v3)

e4 = Egde()
e4.add_egde(v3,v4)

e5 = Egde()
e5.add_egde(v4,v1)

v1.add_egde(e1.connections)
v1.add_egde(e2.connections)
v2.add_egde(e3.connections)
v3.add_egde(e4.connections)


g1 = Graph()

g1.add_vertices(v1)
g1.add_vertices(v2)
g1.add_vertices(v3)
g1.add_vertices(v4)

pprint.pprint(g1.graph)