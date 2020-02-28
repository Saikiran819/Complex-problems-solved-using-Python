
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
        
    def getVertices(self):
        return self.vertexList.keys()
    
    def __iter__(self):
        return iter(self.vertexList.values())

    def __contains__(self, key):
        return key in self.vertexList

def word_ladder():
    dict_of_buckets = {}
    g = graph()
    
    fp = open("word_list.txt", 'r')
    for line in fp:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + "_" + word[i+1:]
            if bucket in dict_of_buckets:
                dict_of_buckets[bucket].append(word)
            else:
                dict_of_buckets[bucket] = [word]
    
    for bucket in dict_of_buckets.keys():
        for word1 in dict_of_buckets[bucket]:
            for word2 in dict_of_buckets[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    
    fp.close
    return g

temp = []
bfs = []
c = 0

#bfs traversal until the target element is found
def bfs_traversal(g, start, end):
    global c
    
    vtx = g.getVertex(start)
    if c == 0:
        bfs.append(vtx)
    if vtx:
        for nbr in vtx.connTo:
            if nbr not in bfs:
                temp.append(nbr)
        if len(temp) > 0:
            beg = temp.pop(0)
            if beg not in bfs:
                bfs.append(beg)
            c = 1
            if beg.id != end:  #This condition can be removed if you want full BFS traversal
                bfs_traversal(g, beg.id, end)

def shortest_path(g, word1, word2):
    global c
    
    if g.getVertex(word1) and g.getVertex(word2):
        
        bfs_traversal(g, word1, word2)
        if len(bfs) > 1:
            for i in range(len(bfs)-1, 1, -1):
                if not bfs[i].isConnTo(bfs[i-1]):
                    bfs.pop(i-1)
            
            for i in range(len(bfs)):
                bfs[i] = bfs[i].id
            print("The shortest path is of length = " + str(len(bfs)))
            print("->".join(bfs) + "\n")
        
        #Empty the list until after every check
        for i in range(len(bfs)):
            if len(bfs) > 0:
                bfs.pop(0)
        #Empty the list until after every check
        for i in range(len(temp)):
            if len(temp) > 0:
                temp.pop(0)
        #Initialize it to zero after every check
        c = 0
    else:
        print("Can't find a path:(\n")

g = word_ladder()
shortest_path(g, "pope", "bull")
shortest_path(g, "ball", "gulf")
shortest_path(g, "nose", "pope")
shortest_path(g, "pope", "miss")
shortest_path(g, "toon", "plea")
shortest_path(g, "full", "toon")
shortest_path(g, "full", "drool")


