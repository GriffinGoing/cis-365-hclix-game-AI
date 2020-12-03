import sys
from math import floor, ceil
sys.path.append('..')
import board

'''

'''
def hasLineOfSight(start, end, board, characterPositions):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

    start = start.lower()
    end = end.lower()

    # parse x and y from start and end
    startX = letters.index(start[0])
    startY = int(start[1:]) - 1
    endX = letters.index(end[0])
    endY = int(end[1:]) - 1

    # calculate the implicit slope of the direct cartesian line from start to end:
    xDelta = endX - startX
    yDelta = endY - startY
    # slope = yDelta/xDelta

    # start from center of "start" within theoretical coordinate coordinate (IE, x.5, y.5)
    currentX = startX + .5
    currentY = startY + .5

    # every iteration, add slope * 1/50 per 1/50th of x change , use FLOOR to grab integer to find the current location,
    # and look for adjacency from last location to this, or that the box is the same as the last
    # IE has not moved

    # the number of times to iterate per single X. For example, for a value of
    # 50, I will perform 50 iterations from the span of A1 to B1 and check LOS at each
    # point in between
    iterationsPerX = 50

    lastNode = board.graph[int(currentX)][int(currentY)]
    currNode = board.graph[int(currentX)][int(currentY)]

    while (currNode.name != end):
        # increment 'pointer' position
        currentX = currentX + (xDelta / iterationsPerX)
        currentY = currentY + (yDelta / iterationsPerX)

        print("currentX: " + str(currentX) + " currentY: " + str(currentY))

        currNode = board.graph[int(currentX)][int(currentY)]
        print("currNode: " + str(currNode.name))

        xCorner = (abs(floor(currentX) - currentX) < .01) or (abs(ceil(currentX) - currentX) < .01)
        yCorner = (abs(floor(currentY) - currentY) < .01) or (abs(ceil(currentY) - currentY) < .01)


        # if a wall obstructs LOS, return False
        if ((lastNode.name != currNode.name) and (lastNode not in currNode.adjacentTo) and (not(xCorner or yCorner))):
            print(start + " LOS to " + end + ": False")
            return False

        # if a character obstructs LOS, return False
        if ((currNode.name != start) and (currNode.name != end) and (currNode.name.upper() not in characterPositions))
            print(start + " LOS to " + end + ": False")
            return False

        lastNode = currNode

    # if no conflict is found in the entiriety of the loops, LOS is true
    print(start + " LOS to " + end + ": True")
    return True



board.main()

hasLineOfSight("d10", "h14", board, characters)

