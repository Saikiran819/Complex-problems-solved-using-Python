
class vertex:
    def __init__(self, key):
        self.id = key
        self.connTo = {}
        
    def addNeighbor(self, nbr, weight = 0):
        self.connTo[nbr] = weight
    
    def getConnenctions(self):
        return self.connTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connTo[nbr]
    
    def __str__(self):
        return str(self.id) + " is connected to" + str([x.id for x in self.connTo])
    
class graph:
    def __init__(self):
        self.vertexList = {}
        self.noOfvertices = 0
    
    def addVertex(self, key):
        newV = vertex(key)
        self.noOfvertices += 1
        self.vertexList[key] = newV
        return newV

    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None
    
    def addEdge(self, frm, to, wt=0):
        if frm not in self.vertexList:
            newV = self.addVertex(frm)
        if to not in self.vertexList:
            newV = self.addVertex(to)
        
        self.vertexList[frm].addNeighbor(self.vertexList[to], wt)
        
    def getVertices(self):
        return self.vertexList.keys()
    
    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self, key):
        return key in self.vertexList

g = graph()

for i in range(1 , 6):
    g.addVertex(i)

g.addEdge(0, 1, 5)
g.addEdge(1, 2, 10)
g.addEdge(2, 3, 15)
g.addEdge(3, 4, 20)
g.addEdge(4, 5, 25)
g.addEdge(5, 0, 30)


for vtx in g:
    print(vtx)
    print(vtx.getConnenctions)
    print('\n')
