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
    
    def isConnTo(self, nbr):
        return nbr in self.connTo
    
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
        self.vertexList[to].addNeighbor(self.vertexList[frm], wt)
        
    def getVertices(self):
        return self.vertexList.keys()
    
    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self, key):
        return key in self.vertexList

dfs = []
temp = []
c = 0
def dfs_traversal(g, start):
    
    global c
    
    vtx = g.getVertex(start)
    if c == 0:
        dfs.append(vtx.id)
        temp.append(vtx.id)
    print(temp)
    
    """
    If the top value doesn't have a nbr or the nbrs are already visited.
    Then pop that vertex and repeat.
    """
    while len(vtx.connTo) == 0 or all([x.id in dfs for x in vtx.connTo]):
        if len(temp) > 0:
            temp.pop(-1)
            if len(temp) > 0:
                vtx = g.getVertex(temp[-1])
        else:
            break
    """
    If the top vertex has a nbr that's not visited yet. Append it to the DFS
    and visit the nbrs of that top vertex.
    """
    
    for nbr in vtx.connTo:
        if nbr.id not in dfs and nbr.id not in temp:
            dfs.append(nbr.id)
            temp.append(nbr.id)
            c = 1
            dfs_traversal(g, temp[-1])


g = graph()
g.addEdge(1, 4)
g.addEdge(1, 2)
g.addEdge(3, 4)
g.addEdge(3, 10)
g.addEdge(9, 3)
g.addEdge(3, 2)
g.addEdge(2, 8)
g.addEdge(7, 8)
g.addEdge(2, 5)
g.addEdge(2, 7)
g.addEdge(5, 8)
g.addEdge(5, 6)
g.addEdge(5, 7)

dfs_traversal(g, 1)


print(temp)
print(dfs)
while len(dfs):
    dfs.pop()

c = 0

g2 = graph()
g2.addEdge(1, 2)
g2.addEdge(1, 3)
g2.addEdge(1, 7)
g2.addEdge(2, 4)
g2.addEdge(2, 6)
g2.addEdge(3, 5)
g2.addEdge(3, 8)
g2.addEdge(4, 7)
g2.addEdge(5, 6)
g2.addEdge(6, 8)
g2.addEdge(7, 8)

dfs_traversal(g2, 5)

print(temp)
print(dfs)