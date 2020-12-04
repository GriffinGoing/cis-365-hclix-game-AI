import Pathing
from math import sqrt,pow,floor,ceil

currentPlayer = 0

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'N', 'P']
Lletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']


class player():
    def __init__(self,characters,p2characters):
        self.actionTotal = 300
        self.points = 0
        self.starterArea = 0
        self.enemyIndex = 2
        self.characters = characters
        self.p2characters = p2characters
    def playerCharactersMove(self,graph,player1chars,player2chars):
        numberDead = 0
        self.characters = player1chars
        self.p2characters = player2chars
        self.actionTotal = 300
        self.graph = graph
        for i in self.characters:

            i = self.characters[i].getCharacter()
            #if character is KO'd then go to next character
            if i['attack'] == 'KO':
                numberDead += 1
                next(i)
            #if Character didn't do an action last turn he loses 1 action token on this turn
            if i['didAction'] == False:
                i['didAction'] = 0
            #if character has two action tokens they cannot do anything this turn
            if i['didAction'] == 2:
                next(i)

            #characters x,y position
            #pos = [letters.index[i.position[0]],int(i.position[1])-1]

            actions,target = self.chooseTarget(i,self.graph)
            print(actions)
            if actions['cost'][0] == 'cost':
                i['actionToken'] += 1
                self.actionTotal -= 100

            if actions['move'][0] == True:
                self.move(i,target['position'],actions['move'][1],self.graph)
            if actions['attack'][0] == True:
                atkDamage = i['damage']
                type = actions['attack'][1]
                if type == 'Range' and actions['special'][1] == 'Range Combat Expert':
                    atkDamage += 2
                if type == 'Close':
                    if actions['special'][1] == 'Close Combat Expert':
                        atkDamage += 2
                    if i['attackAbility'] == 'Super Strength':
                        print('Will KnockBack if target Hit ')
                print('attack with ' + actions['attack'][1] + 'for ' + str(atkDamage) + 'damage \n Please roll' )

            if actions['cost'] == 'cost':
                i['didAction'] += 1
            #if the character is pushed then he always takes 1 click of damage
            if i['didAction'] == 2:
                i['click'] += 1

        if numberDead == 3:
            exit()

    # move and attack are in player class because only the player should move their pieces
    def move(self,character,target,moveAmount,board):

        path = Pathing.AStarAlgo(character['position'],target,moveAmount,board,character['canFly'])
        for i in path:
            print(i.name, end='->')
        print()
    # Decides what attack to launch at enemy target, rolls for damage, can miss,critically miss,hit,critically hit
    # def attack(self,character,enemyTarget):
    #     damage = 0
    #     hitChance = 0
    #
    #     diceRoll1 = rollDice(0,6)
    #     diceRoll2 = rollDice(0,6)
    #
    #     if diceRoll1 == 1 and diceRoll2 == 1:
    #         character.click += 1
    #
    #     if diceRoll1 == 6 and diceRoll2 == 6:
    #         damage += 1
    #
    #     #For all methods of attack, calculate damage and hitchance and choose best combo of both
    #     #aka choose biggest number and do that
    #
    #     return 'hi'

    #checks to see if can destroy wall, if it can then return True, if not return False, no ranged wall break as of now

    def destroyWall(self,character,wallx,wally,direction):
        if character.position[1] == wallx and character.position[2] == wally:
            return True
        else:
            return False

    # Decides which target a character should move towards and attack
    # Priority is : 1=LOS and in range, 2=lowest range that has lowest health
    def chooseTarget(self,char,graph):

        lowDistTarget = 0
        lowDistTargetHealth = 15
        pos = [Lletters.index(char['position'][0]) , int(char['position'][1:])-1]
        posString = char['position']
        allCharPositions = [self.characters['Captain America'].getCharacter()['position'],self.characters['Thor'].getCharacter()['position'],
                            self.characters['Iron Man'].getCharacter()['position'],
                            self.p2characters['Captain America'].getCharacter()['position'], self.p2characters['Thor'].getCharacter()['position'],
                            self.p2characters['Iron Man'].getCharacter()['position']]

        chosenEnemy = -1
        chosenEnemyHealth = -10
        targetLOSStatus = False
        targetInRangeStatus = False
        distance = 100
        for i in self.p2characters:
            i = self.p2characters[i].getCharacter()
            if i['attack'] == 'KO':
                next(i)
            inRange = False
            enemyPos = []
            enemyX = Lletters.index(i['position'][0])

            enemyY  = int(i['position'][1:])-1
            enemyPos.append(enemyX)
            enemyPos.append(enemyY)
            #gets hypotenuse distance between current character and the enemy character
            defDistance = floor(sqrt(pow(abs(pos[0]-enemyPos[0]), 2) + pow(abs(pos[1]-enemyPos[1]), 2)))
            if defDistance <= char['range']:
                inRange = True
            inLOS = self.lineOfSight(posString,i['position'],graph,allCharPositions)

            #if someone is in range, has los then they are the target

            if inRange == True and inLOS == True and i['click'] > chosenEnemyHealth:
                chosenEnemy = i
                chosenEnemyHealth = i['click']
                targetLOSStatus = True
                targetInRangeStatus = True
                distance = defDistance

            elif defDistance <= distance and i['click'] < lowDistTargetHealth and chosenEnemy == -1:
                distance = defDistance
                lowDistTargetHealth = i['click']
                lowDistTarget = i
                targetInRangeStatus = True
        if chosenEnemy == -1:
            chosenEnemy = lowDistTarget

        return self.characterActions(char,distance,targetLOSStatus,targetInRangeStatus),chosenEnemy

    # Decides if a character should even move or attack this turn
    def characterActions(self,character,dist,inLOS,inRange):
        decisions = {'move' : [False,0], 'attack':[False,'Close'],'special':[False,0],'cost':'free'}

        '''
        Dist = distance away from target the character is
        Ranged attacks cant be used when adjacent to enemy aka if dist == 1
        '''

        #determines whether it can use Running Shot
        # if character['speedAbility'] == 'Running Shot' and ((dist - ceil(character['speed']/2)) < character['range'])\
        #         and character['actionToken'] < 2 and (dist - ceil(character['speed']/2)) > 1:
        #     decisions['special'][0] = True
        #     decisions['move'] = [True,ceil(character['speed']/2)]
        #     decisions['attack'] = [True,'Range']
        #     decisions['cost'] = 'cost'


        #Determines whether it can use charge
        if dist < ceil(character['speed']/2) and (character['speedAbility'] == 'Charge') \
                and (character['damageAbility'] == "Close Combat Expert") and character['actionToken'] < 2:
            decisions['special'][0] = True
            decisions['move'] = [True, ceil(character['speed'] / 2)]
            decisions['attack'] = [True,'Close']
            decisions['cost'] = 'cost'
        #determines whether it can attack in ranged

        elif dist < character['range'] and dist > 1 and inLOS == True and character['actionToken'] < 2:
            decisions['attack'] = [True, 'Range']
            decisions['cost'] = 'cost'
            if character['damageAbility'] == 'Range Combat Expert':
                decisions['special'] = [True, character['damageAbility']]

        #determines whether it should sidestep to attack in range currently not in use due to being hard to implement running away
        # elif dist == 1 and character['speedAbility'] == 'Sidestep' and character['damageAbility'] == 'Range Combat Expert':
        #     decisions['special'] = [True,'Sidestep','Range Combat Expert']
        #     decisions['move'] = [True,2]
        #     decisions['cost'] = 'free'

        #determines whether it should attack in melee
        elif dist == 1 and character['actionToken'] < 2 and inLOS == True:
            decisions['attack'] = [True, 'Close']
            decisions['cost'] = 'cost'
            if character['damageAbility'] == 'Close Combat Expert':
                decisions['special'] = [True, character['damageAbility']]
        #moves because it can't do any of the above
        elif character['actionToken'] < 2 and (dist >= 2 or inLOS == False) :
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
        lastNode = board[int(currentX)][int(currentY)]
        currNode = board[int(currentX)][int(currentY)]
        while (currNode.name != end):
            # increment 'pointer' position
            currentX = currentX + (xDelta / iterationsPerX)
            currentY = currentY + (yDelta / iterationsPerX)


            currNode = board[int(currentX)][int(currentY)]

            xCorner = (abs(floor(currentX) - currentX) < .01) or (abs(ceil(currentX) - currentX) < .01)
            yCorner = (abs(floor(currentY) - currentY) < .01) or (abs(ceil(currentY) - currentY) < .01)

            # if a wall obstructs LOS, return False
            if ((lastNode.name != currNode.name) and (lastNode not in currNode.adjacentTo) and (
            not (xCorner or yCorner))):
                return False

            # if a character obstructs LOS, return False
            if (currNode.name != start) and (currNode.name != end):
                if (currNode.name.upper() in characterPositions):
                    return False

            lastNode = currNode

            # if no conflict is found in the entiriety of the loops, LOS is true
        return True

# creates
def main(player1Char,player2Char):
    player1 = player(player1Char,player2Char)
    global currentPlayer
    currentPlayer = player1


def nextTurn(player1Char,player2Char,Board):
    #global players
    #players = []
    #players.append(player1Char)
    #players.append(player2Char)
    graph = Board
    currentPlayer.playerCharactersMove(graph,player1Char,player2Char)

