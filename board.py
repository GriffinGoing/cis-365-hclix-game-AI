from enum import Enum


rows, cols = (16, 16)
graph = [[0 for i in range(cols)] for j in range(rows)]

class walls(Enum):
    n = 0
    e = 1
    s = 2
    w = 3

class node:
    def __init__(self, name,terrain, adjacentTo, walls):
        self.name = name
        self.type = terrain
        self.adjacentTo = adjacentTo
        self.walls = walls


def buildGraph():

      # dictionary of nodes

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for col in range(cols):
        for row in range(rows):
            nodeName = letters[col] + str(row+1)
            graph[col][row] = node(nodeName,None,0,0)

            
            
            
    #Calculates each nodes adjacent node
    #will later include wall checking and if a wall exists on possible adjacent nodes dont add them
    for col in range(cols):
        for row in range(rows):
            adjacent = []
            for i in range(col-1,col+2):
                if (0 <= i <= 15) and row-1 >= 0:
                    adjacent.append(graph[i][row-1])
                if (0 <= i <= 15) and row+1 <= 15:
                    adjacent.append(graph[i][row+1])
            if col-1 >= 0:
                adjacent.append(graph[col-1][row])
            if col+1 <= 15:
                adjacent.append(graph[col+1][row])
            graph[col][row].adjacentTo = adjacent





#building board
buildGraph()


#some testing to see if all the adjacent nodes were corrent
for i in range(cols):
    for j in range(rows):
        print(graph[i][j].name,end='->')
        node = graph[i][j]
        for k in node.adjacentTo:
            print(k.name,end=', ')
        print()



