import gameGUI
import Pathing
from random import randint
from math import sqrt,pow,floor,ceil

global currentPlayer

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'N', 'P']

class player():
    def __init__(self,position):
        self.actionTotal = 300
        self.position = position
        self.points = 0
        self.starterArea = 0
        #self.characters = gameGUI.player1Chars
        self.enemyIndex = 2


    def playerCharactersMove(self,graph):
        numberDead = 0
        self.actionTotal = 300

        for i in self.characters:
            #here to show if the character has taken a costed action this move
            costedAction = False
            #Here to see if the character is allowed to do a double power this move
            DoublePower = False

            if i.actionToken == 0:
                DoublePower = True

            #if character is KO'd then go to next character
            if i.attackVal == 'KO':
                numberDead += 1
                next(self.characters)
            #if Character didn't do an action last turn he loses 1 action token on this turn
            if i.didAction == False:
                i.actionToken = 0
            #if character has two action tokens they cannot do anything this turn
            if i.actionToken == 2:
                next(self.characters)

            #characters x,y position
            pos = [letters.index[i.position[0]],int(i.position[1])-1]

            actions,target = self.chooseTarget(i,graph)
            print(actions)
            if actions['cost'][0] == 'cost':
                i.actionToken += 1
                self.actionTotal -= 100

            if actions['move'][0] == True:
                self.move(i,target,actions['move'][1])
            if actions['attack'][0] == True:
                print('attack with ' + actions['attack'][1])

            #if the character is pushed then he always takes 1 click of damage
            if i.actionToken == 2:
                i.click += 1

        if numberDead == 3:
            admitDefeat(self.position,self.points)

    # move and attack are in player class because only the player should move their pieces
    def move(self,character,target,moveAmount):
        start = 0
        path = Pathing.AStarAlgo(start,target,moveAmount,gameGUI.board,character.canFly)
        print(path)

    # Decides what attack to launch at enemy target, rolls for damage, can miss,critically miss,hit,critically hit
    def attack(self,character,enemyTarget):
        damage = 0
        hitChance = 0

        diceRoll1 = rollDice(0,6)
        diceRoll2 = rollDice(0,6)

        if diceRoll1 == 1 and diceRoll2 == 1:
            character.click += 1

        if diceRoll1 == 6 and diceRoll2 == 6:
            damage += 1

        #For all methods of attack, calculate damage and hitchance and choose best combo of both
        #aka choose biggest number and do that

        return 'hi'

    #checks to see if can destroy wall, if it can then return True, if not return False, no ranged wall break as of now
    def destroyWall(self,character,wallx,wally,direction):
        if character.position[1] == wallx and character.position[2] == wally:
            return True
        else:
            return False

    # Decides which target a character should move towards and attack
    # Priority is : 1=LOS and in range, 2=lowest range that has lowest health
    def chooseTarget(self,pos,char,graph):
        lowDistTarget = 0
        lowDistTargetHealth = 15
        start = letters[pos[0]] + str(pos[1]+1)
        allCharPositions = 0

        chosenEnemy = -1
        chosenEnemyHealth = 15
        targetLOSStatus = False
        targetInRangeStatus = False
        distance = 100
        for i in players[1]:
            inRange = False
            enemyPos = [letters.index[i.position[0]],int(i.position[1])-1]
            #gets hypotenuse distance between current character and the enemy character
            defDistance = floor(sqrt(pow(abs(pos[0]-enemyPos[0]), 2) + pow(abs(pos[1]-enemyPos[1])), 2))
            if defDistance <= char['range']:
                inRange = True
            inLOS = self.lineOfSight(start,i.position,graph,allCharPositions)

            #if someone is in range, has los then they are the target
            if inRange == True and inLOS == True and i.click < chosenEnemyHealth:
                chosenEnemy = i
                chosenEnemyHealth = i.click
                targetLOSStatus = True
                targetInRangeStatus = True

            elif defDistance <= distance and i.click < lowDistTargetHealth and chosenEnemy == -1:
                distance = defDistance
                lowDistTargetHealth = i.click
                lowDistTarget = i
                targetInRangeStatus = True


        if chosenEnemy == -1:
            chosenEnemy = lowDistTarget

        return self.characterActions(char,distance,targetLOSStatus,targetInRangeStatus),chosenEnemy

    # Decides if a character should even move or attack this turn
    def characterActions(self,character,dist,inLOS,inRange):
        decisions = {'move' : [False,0], 'attack':[False,'Close'],'special':False,'cost':'free'}

        #determines whether it can use Running Shot
        if character['speedAbility'] == 'Running Shot' and ((dist - ceil(character['speed']/2)) < character['range'])\
                and character.actionTokens < 2:
            decisions['special'] = True
            decisions['move'] = [True,ceil(character['speed']/2)]
            decisions['attack'] = [True,'Range']
            decisions['cost'] = 'cost'

        #Determines whether it can use charge
        elif dist < ceil(character['speed']/2) and (character['speedAbility'] == 'Charge') \
                and (character['damageAbility'] == "Close Combat Expert") and character.actionTokens < 2:
            decisions['special'] = True
            decisions['move'] = [True, ceil(character['speed'] / 2)]
            decisions['attack'] = [True,'Close']
            decisions['cost'] = 'cost'
        #determines whether it can attack in ranged
        elif dist < character['range'] and dist > 1 and inLOS == True and character.actionTokens < 2:
            decisions['attack'] = [True, 'Range']
            decisions['cost'] = 'cost'
        #determines whether it should sidestep to attack in range
        elif dist == 1 and character['speedAbility'] == 'Sidestep' and character['damageAbility'] == 'Range Combat Expert':
            decisions['special'] = True
            decisions['move'] = [True,2]
            decisions['cost'] = 'free'
        #determines whether it should attack in melee
        elif dist == 1 and character.actionTokens < 2:
            decisions['attack'] = [True, 'Close']
            decisions['cost'] = 'cost'
        #moves because it can't do any of the above
        elif character.actionTokens < 2 and dist > 1:
            decisions['move'] = [True,character['speed']]
            decisions['cost'] = 'cost'
        return decisions

    #determines if character is within LOS of enemy to begin attack
    def lineOfSight(self,start,end,board,characterPositions):
        Lletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

        start = start.lower()
        end = end.lower()

        # parse x and y from start and end
        startX = Lletters.index(start[0])
        startY = int(start[1:]) - 1
        endX = Lletters.index(end[0])
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


            currNode = board.graph[int(currentX)][int(currentY)]

            xCorner = (abs(floor(currentX) - currentX) < .01) or (abs(ceil(currentX) - currentX) < .01)
            yCorner = (abs(floor(currentY) - currentY) < .01) or (abs(ceil(currentY) - currentY) < .01)

            # if a wall obstructs LOS, return False
            if ((lastNode.name != currNode.name) and (lastNode not in currNode.adjacentTo) and (
            not (xCorner or yCorner))):
                return False

            # if a character obstructs LOS, return False
            if ((currNode.name != start) and (currNode.name != end) and (
                    currNode.name.upper() not in characterPositions)):
                return False

            lastNode = currNode

            # if no conflict is found in the entiriety of the loops, LOS is true
        return True




def admitDefeat(loser,points):
    winner = players[loser.enemyIndex]
    print('player' + str(loser.position) + 'has lost the game while only getting ' + str(loser.points)+ 'points.'
          'Player ' + str(loser.enemyIndex) + 'has won the game with 300 points')


# roll dice                : NOT USED
def rollDice(start,end):
    return randint(start,end)

# creates
def main():
    player1 = player(1)
    player2 = player(2)
    global players
    players = [player1, player2]


def nextTurn(player1Char,player2Char,Board):
    players[0].characters = player1Char
    players[1].characters = player2Char
    graph = Board
    players[0].playerCharactersMove(graph)


if __name__ == '__main__':
    main()
