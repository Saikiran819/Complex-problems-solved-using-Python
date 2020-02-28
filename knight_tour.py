class vertex:
    def __init__(self, key):
        self.id = key
        self.connTo = {}
        
    def addNeighbor(self, nbr, weight = 0):
        self.connTo[nbr] = weight
    
    def getConnenctions(self):
        return self.connTo.keys()
    
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


chess_board = [["idx"+str(j)+str(i) for i in range(8)] for j in range(8)]
def board_graph():
    g = graph()
    move_x = [1, 1, 2, 2, -1, -1, -2, -2]
    move_y = [2, -2, 1, -1, 2, -2, 1, -1]

    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            for k in range(len(move_x)):
                new_x = i + move_x[k]
                new_y = j + move_y[k]
                if new_x in range(len(chess_board)) and new_y in range(len(chess_board)):
                    g.addEdge(chess_board[i][j], chess_board[new_x][new_y])

    return g
                    
g = board_graph()

init = 0
dfs = []
temp = []
def knight_tour(rowid, colid):
     global init
     
     idx = "idx"+str(rowid)+str(colid)
     
     vtx = g.getVertex(idx)
     if init == 0:
        dfs.append(vtx.id)
        temp.append(vtx.id)
     while len(vtx.connTo) == 0 or all([x.id in dfs for x in vtx.connTo]):
        if len(temp) > 0:
            temp.pop(-1)
            if len(temp) > 0:
                vtx = g.getVertex(temp[-1])
        else:
            break
     for nbr in vtx.connTo:
         if nbr.id not in dfs and nbr.id not in temp:
             dfs.append(nbr.id)
             temp.append(nbr.id)
             init = 1
             knight_tour(int(nbr.id[3]), int(nbr.id[4]))

knight_tour(0,0)

#print(dfs)

step = 1
for k in range(len(dfs)):
    chess_board[int(dfs[k][3])][int(dfs[k][4])] = str(step)
    step+=1

for rows in chess_board:
        print("\t".join(rows))
        print("\n")