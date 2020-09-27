import board


#making the heroclix board in pathfinding
board = board.main()


#start and end parameters will be node id's
#Ex. start = a1 , end = p13
def AStarAlgo(start,end):

    startNode =board[ord(start[0]) - 97][int(start[1:len(start)])-1]
    endNode = board[ord(end[0]) - 97][int(end[1:len(end)])-1]

    #Q is a queue
    Q = []
    Q.append(startNode)

    Path = []

    while len(Q) > 0:
        G = Q.pop(0)
        if G == endNode:
            Path.append(G)
            return Path
        else:
            Path.append(G)
            min = 500
            minNode = 0;
            for node in G.adjacentTo:
                nodeX = abs((ord(node.name[0]) - 97) - (ord(end[0]) - 97))
                nodeY = abs((int(node.name[1:len(node.name)])-1) - (int(end[1:len(end)])-1))
                distance = (nodeX) + (nodeY)
                futureNode = nextNodeWeight(node,endNode.name)
                weight = distance - (len(node.adjacentTo)/4)
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
            if(minNode != 0):
                Q.append(minNode)

    return Path

def nextNodeWeight(rootNode, end):
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


'''
Insert A star algorithm testing here

To add test cases do:
    path = AStarAlgo(StartNode.Name,EndNode.name)
    if path != False:
        print(path)
    else:
        print('your algo sucks or your input sucks')
'''

path = AStarAlgo('a1','p16')
if path != False:
    count = 0
    for i in path:
        print(i.name,end='->')
        count += 1
        if count > 10:
            print()
            count = 0
else:
    print('your algo sucks or your input sucks')