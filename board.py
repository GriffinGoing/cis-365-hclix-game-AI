from enum import Enum


rows, cols = (16, 16)
graph = [[0 for i in range(cols)] for j in range(rows)]

class directions(Enum):
    NORTH = 0
    EAST = 1
    SOUTH =2
    WEST = 3

    def interpet(self):
        return 0

class node:
    def __init__(self, name,terrain, adjacentTo, northWall = False, eastWall = False, southWall = False, westWall = False):
        self.name = name
        self.terrain = terrain
        self.adjacentTo = adjacentTo
        self.walls = {
            directions.NORTH: northWall,
            directions.EAST: eastWall,
            directions.SOUTH: southWall,
            directions.WEST: westWall,
        }


def buildGraph():

      # dictionary of nodes

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    for col in range(cols):
        for row in range(rows):
            nodeName = letters[col] + str(row+1)
            graph[col][row] = node(nodeName,'normal',0)

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



def addTerrain():
    for col in range(0,3):
        for row in range(0,3):
            graph[col][row].terrain = 'start'
            graph[col+13][row].terrain = 'start'
            graph[col+13][row+13].terrain = 'start'
            graph[col][row+13].terrain = 'start'

    for col in range(4,7):
        graph[col][0].terrain = 'water'
        graph[col+5][0].terrain = 'water'
    graph[6][1].terrain = 'water'
    graph[9][1].terrain = 'water'
    for col in range(6,10):
        graph[col][2].terrain = 'water'
    graph[7][5].terrain = 'water'
    for col in range(6,10):
        for row in range(6,10):
          continue

def addWalls():
    for row in range(4, 8):
        temp = graph[1][row]
        temp.walls[directions.EAST] = True
        temp = graph[2][row]
        temp.walls[directions.WEST] = True

    for row in range(9, 12):
        temp = graph[1][row]
        temp.walls[directions.EAST] = True
        temp = graph[2][row]
        temp.walls[directions.WEST] = True

    for row in range(2, 5):
        temp = graph[3][row]
        temp.walls[directions.EAST] = True
        temp = graph[4][row]
        temp.walls[directions.WEST] = True

    for row in range(11, 15):
        temp = graph[3][row]
        temp.walls[directions.EAST] = True
        temp = graph[4][row]
        temp.walls[directions.WEST] = True

    for row in range(1, 2):
        temp = graph[5][row]
        temp.walls[directions.EAST] = True
        temp = graph[6][row]
        temp.walls[directions.WEST] = True

    for row in range(4, 8):
        temp = graph[5][row]
        temp.walls[directions.EAST] = True
        temp = graph[6][row]
        temp.walls[directions.WEST] = True

    for row in range(9, 11):
        temp = graph[5][row]
        temp.walls[directions.EAST] = True
        temp = graph[6][row]
        temp.walls[directions.WEST] = True

    for row in range(12, 14):
        temp = graph[5][row]
        temp.walls[directions.EAST] = True
        temp = graph[6][row]
        temp.walls[directions.WEST] = True

    for row in range(0, 3):
        temp = graph[7][row]
        temp.walls[directions.EAST] = True
        temp = graph[8][row]
        temp.walls[directions.WEST] = True

    for row in range(12, 16):
        temp = graph[7][row]
        temp.walls[directions.EAST] = True
        temp = graph[8][row]
        temp.walls[directions.WEST] = True

    for row in range(1, 2):
        temp = graph[9][row]
        temp.walls[directions.EAST] = True
        temp = graph[10][row]
        temp.walls[directions.WEST] = True

    for row in range(6, 9):
        temp = graph[9][row]
        temp.walls[directions.EAST] = True
        temp = graph[10][row]
        temp.walls[directions.WEST] = True

    for row in range(12, 13):
        temp = graph[10][row]
        temp.walls[directions.EAST] = True
        temp = graph[11][row]
        temp.walls[directions.WEST] = True

    for row in range(14, 16):
        temp = graph[10][row]
        temp.walls[directions.EAST] = True
        temp = graph[11][row]
        temp.walls[directions.WEST] = True

    for row in range(2, 4):
        temp = graph[11][row]
        temp.walls[directions.EAST] = True
        temp = graph[12][row]
        temp.walls[directions.WEST] = True

    for row in range(4, 6):
        temp = graph[13][row]
        temp.walls[directions.EAST] = True
        temp = graph[14][row]
        temp.walls[directions.WEST] = True

    for row in range(10, 12):
        temp = graph[13][row]
        temp.walls[directions.EAST] = True
        temp = graph[14][row]
        temp.walls[directions.WEST] = True

    for col in range(4, 6):
        temp = graph[col][1]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][2]
        temp.walls[directions.NORTH] = True

    for col in range(10, 12):
        temp = graph[col][1]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][2]
        temp.walls[directions.NORTH] = True

    for col in range(2, 4):
        temp = graph[col][3]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][4]
        temp.walls[directions.NORTH] = True

    for col in range(6, 7):
        temp = graph[col][3]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][4]
        temp.walls[directions.NORTH] = True

    for col in range(10, 14):
        temp = graph[col][3]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][4]
        temp.walls[directions.NORTH] = True

    for col in range(7, 12):
        temp = graph[col][5]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][6]
        temp.walls[directions.NORTH] = True

    for col in range(14, 15):
        temp = graph[col][5]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][6]
        temp.walls[directions.NORTH] = True

    for col in range(2, 4):
        temp = graph[col][6]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][7]
        temp.walls[directions.NORTH] = True

    for col in range(12, 16):
        temp = graph[col][7]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][8]
        temp.walls[directions.NORTH] = True

    for col in range(0, 4):
        temp = graph[col][8]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][9]
        temp.walls[directions.NORTH] = True

    for col in range(6, 8):
        temp = graph[col][9]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][10]
        temp.walls[directions.NORTH] = True

    for col in range(9, 12):
        temp = graph[col][9]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][10]
        temp.walls[directions.NORTH] = True

    for col in range(14, 15):
        temp = graph[col][9]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][10]
        temp.walls[directions.NORTH] = True

    for col in range(2, 3):
        temp = graph[col][11]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][12]
        temp.walls[directions.NORTH] = True

    for col in range(10, 14):
        temp = graph[col][11]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][12]
        temp.walls[directions.NORTH] = True

    for col in range(4, 6):
        temp = graph[col][13]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][14]
        temp.walls[directions.NORTH] = True

    for col in range(8, 9):
        temp = graph[col][13]
        temp.walls[directions.SOUTH] = True
        temp = graph[col][14]
        temp.walls[directions.NORTH] = True

    #four squares in the middle
    graph[7][7].walls[directions.NORTH] = True
    graph[7][7].walls[directions.WEST] = True

    graph[8][7].walls[directions.NORTH] = True
    graph[8][7].walls[directions.EAST] = True

    graph[7][8].walls[directions.SOUTH] = True
    graph[7][8].walls[directions.WEST] = True

    graph[8][8].walls[directions.SOUTH] = True
    graph[8][8].walls[directions.EAST] = True

def removeWallAdjacencies():
    for col in range(cols):
        for row in range(rows):
            removeNE = False
            removeNW = False
            removeSE = False
            removeSW = False
            temp = graph[col][row]

            #north, nw, ne, and double-north-wall adjacencies
            if (temp.walls[directions.NORTH] and row > 0):
                #print(graph[col][row-1].name)
                nodeToRemove = graph[col][row - 1]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

                #ne corner
                removeNE = (temp.walls[directions.EAST] and col < 15) or (col < 15 and graph[col+1][row].walls[directions.NORTH])

                #nw corner
                removeNW = (temp.walls[directions.WEST] and col > 0) or (col > 0 and graph[col - 1][row].walls[directions.NORTH])


            #south, sw, se, and double-south-wall adjacencies
            if (temp.walls[directions.SOUTH] and row < 15):
                #print(graph[col][row-1].name)
                nodeToRemove = graph[col][row+1]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

                #se corner
                removeSE = (temp.walls[directions.EAST] and col < 15) or (col < 15 and graph[col+1][row].walls[directions.SOUTH])

                #sw corner
                removeSW = (temp.walls[directions.WEST] and col > 0) or (col > 0 and graph[col - 1][row].walls[directions.SOUTH])

            '''
            Ayden: You had all the stuff below within the south,sw,se, etc if statement check and it
            wasnt removing some of the correct nodes, I think i fixed it without breaking anything?
            '''

            #east and double-east-walls
            if (temp.walls[directions.EAST] and col < 15):
                # print(graph[col][row-1].name)
                nodeToRemove = graph[col+1][row]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

                #ne
                if (row > 0 and graph[col][row-1].walls[directions.EAST]):
                    removeNE = True

                #se
                if (row < 15 and graph[col][row+1].walls[directions.EAST]):
                    removeSE = True

            #west and double-west-walls
            if (temp.walls[directions.WEST] and col > 0):
                # print(graph[col][row-1].name)
                nodeToRemove = graph[col-1][row]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

                # nw
                if (row > 0 and graph[col][row - 1].walls[directions.WEST]):
                    removeNW = True

                # sw
                if (row < 15 and graph[col][row + 1].walls[directions.WEST]):
                    removeSW = True


            #remove NE
            if (removeNE):
                nodeToRemove = graph[col+1][row-1]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

            #remove NW
            if (removeNW):
                nodeToRemove = graph[col - 1][row - 1]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

            #remove SE
            if (removeSE):
                nodeToRemove = graph[col + 1][row + 1]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)

            #remove SW
            if (removeSW):
                nodeToRemove = graph[col-1][row+1]
                if nodeToRemove in temp.adjacentTo:
                    temp.adjacentTo.remove(nodeToRemove)
    for c in range(0,16):
        for r in range(0,16):
            temp = graph[c][r]
            clone = graph[c][r].adjacentTo[:]
            for nodes in clone:
                if nodes.adjacentTo.count(temp) == 0:
                    temp.adjacentTo.remove(nodes)






def printAdj(col, row):
    temp = graph[col][row]
    print("Adj To - - - " + temp.name)
    for node in temp.adjacentTo:
        print(node.name, end=', ')
    print()


# Nothing but side effects, baby. Quality programming here.
def removeWall(col,row,wall):
    if wall == 'east':
        graph[col][row].walls[directions.EAST] = False
        graph[col+1][row].walls[directions.WEST] = False
        addAdj(col+1,row)
    if wall == 'south':
        graph[col][row].walls[directions.SOUTH] = False
        graph[col][row + 1].walls[directions.NORTH] = False
        addAdj(col,row+1)
    if wall == 'west':
        graph[col][row].walls[directions.WEST] = False
        graph[col - 1][row].walls[directions.EAST] = False
        addAdj(col-1,row)
    if wall == 'north':
        graph[col][row].walls[directions.NORTH] = False
        graph[col][row - 1].walls[directions.SOUTH] = False
        addAdj(col,row-1)

    addAdj(col,row)
    removeWallAdjacencies()
def addAdj(col,row):
    node = graph[col][row]
    if row > 0:
        if col > 0:
            if node not in graph[col - 1][row - 1].adjacentTo:
                node.adjacentTo.append(graph[col - 1][row - 1])
                graph[col - 1][row - 1].adjacentTo.append(node)
            if node not in graph[col][row - 1].adjacentTo:
                node.adjacentTo.append(graph[col][row - 1])
                graph[col][row - 1].adjacentTo.append(node)
            if col < 15:
                if node not in graph[col + 1][row - 1].adjacentTo:
                    node.adjacentTo.append(graph[col + 1][row - 1])
                    graph[col + 1][row - 1].adjacentTo.append(node)
    if col > 0:
        if graph[col][row] not in graph[col - 1][row].adjacentTo:
            node.adjacentTo.append(graph[col - 1][row])
            graph[col - 1][row].adjacentTo.append(node)
    if col < 15:
        if node not in graph[col + 1][row].adjacentTo:
            node.adjacentTo.append(graph[col + 1][row])
            graph[col + 1][row].adjacentTo.append(node)

    if row < 15:
        if col > 0:
            if node not in graph[col - 1][row + 1].adjacentTo:
                node.adjacentTo.append(graph[col - 1][row + 1])
                graph[col - 1][row + 1].adjacentTo.append(node)
            if node not in graph[col][row + 1].adjacentTo:
                node.adjacentTo.append(graph[col][row + 1])
                graph[col][row + 1].adjacentTo.append(node)
            if col < 15:
                if node not in graph[col + 1][row + 1].adjacentTo:
                    node.adjacentTo.append(graph[col + 1][row + 1])
                    graph[col + 1][row + 1].adjacentTo.append(node)
def main():
    buildGraph()
    addTerrain()
    addWalls()
    removeWallAdjacencies()
    removeWall(7,1,'east')
    return graph

main()
