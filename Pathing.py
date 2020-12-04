import board
#making the heroclix board in pathfinding
#start and end parameters will be node id's
#Ex. start = a1 , end = p13

def AStarAlgo(start,end,moveLimit,board,fly):
    startNode = board[ord(start[0]) - 97][int(start[1:len(start)])-1]
    endNode = board[ord(end[0]) - 97][int(end[1:len(end)])-1]
    #Q is a queue
    Q = []
    Q.append(startNode)
    Path = []

    while len(Q) > 0:
        if len(Path) >= moveLimit:
            return Path
        G = Q.pop()
        if G == endNode:
            Path.append(G)
            return Path
        else:
            Path.append(G)
            min = 500
            minNode = 0
            for node in G.adjacentTo:
                nodeX = abs((ord(node.name[0]) - 97) - (ord(end[0]) - 97)) * 1.5
                nodeY = abs((int(node.name[1:len(node.name)])-1) - (int(end[1:len(end)])-1)) * 1.5
                distance = (nodeX) + (nodeY)
                futureNode = nextNodeWeight(node,endNode.name,board)

                weight = distance - (len(node.adjacentTo)/2)

                if futureNode > weight:
                    weight = 499
                if futureNode == 0:
                    weight = -100
                if futureNode == -100:
                    weight = -200
                if weight < min:
                    if Path.count(node) == 0:
                        minNode = node
                        min = weight
            #if G.terrain != 'water' and node.terrain == 'water':
            #    return Path
            if node.terrain == 'water' and fly == False:
                moveLimit -= 1
            if(minNode != 0):
                Q.append(minNode)
    return Path

def nextNodeWeight(rootNode, end,board):
    weight = 100
    endNode = board[ord(end[0]) - 97][int(end[1:len(end)]) - 1]

    if rootNode == endNode:
        return -100
    # Q is a queue

    min = 100
    for node in rootNode.adjacentTo:
        nodeX = abs((ord(node.name[0]) - 97) - (ord(end[0]) - 97))
        nodeY = abs((int(node.name[1:len(node.name)]) - 1) - (int(end[1:len(end)]) - 1))
        distance = (nodeX) + (nodeY)
        weight = distance - len(node.adjacentTo) / 4
        if distance == 0:
            return 0
        if weight < min:
                min = weight
    return weight

