import gameGUI
import Pathing
from random import randint

global currentPlayer
global players

class player():
    def __init__(self,position):
        self.actionTotal = 300
        self.position = position
        self.points = 0
        self.starterArea = 0
        self.characters = gameGUI.player1Chars
        self.enemyIndex = 2


    def playerCharactersMove(self):
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
                i.actionToken -= 1
            #if character has two action tokens they cannot do anything this turn
            if i.actionToken == 2:
                next(self.characters)

            #characters x,y position             PLACEHOLDER VALUE
            positionx,positiony = 0


            enemyTarget = self.chooseTarget(i)
            self.move(i,positionx,enemyTarget)
            self.attack(i,enemyTarget)

            #if character makes a costed action his action tokens go up by one
            if costedAction == True:
                i.actionToken += 1
                self.actionTotal -= 100

            #if the character is pushed then he always takes 1 click of damage
            if i.actionToken == 2:
                i.click += 1

        if numberDead == 3:
            admitDefeat(self.position,self.points)

    # move and attack are in player class because only the player should move their pieces
    def move(self,character,start,end):
        moveLimit = self.characters[character].speedVal

        canGetThere,moves = Pathing.AStarAlgo(start,end,moveLimit,gameGUI.board,character.canFly)
        return 'hi'

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
    def chooseTarget(self,character):

        health = 0
        distance = 0
        return 'hi'

    # Decides if a character should even move or attack this turn
    def characterActions(self,character):
        decisions = {'move' : False, 'attack':False,}
        return decisions

    #determines if character is within LOS of enemy to begin attack
    def lineOfSight(self,character,targetx,targety):

        #enemy is in an adjacent tile, LOS = True
        #else if character
        return 'hi'




def admitDefeat(loser,points):
    winner = players[loser.enemyIndex]
    print('player' + str(loser.position) + 'has lost the game while only getting ' + str(loser.points)+ 'points.'
          'Player ' + str(loser.enemyIndex) + 'has won the game with 300 points')



# roll dice
def rollDice(start,end):
    return randint(start,end)

# creates
def main():
    GUI = gameGUI.main()
    player1 = player(1)
    player2 = player(2)
    players = [player1,player2]
    currentPlayer = 1

def nextTurn():
    players[0].playerCharactersMove


if __name__ == '__main__':
    main()
