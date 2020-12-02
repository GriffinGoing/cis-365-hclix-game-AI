import gameGUI
import Pathing
from random import randint

global currentPlayer
global players

class player():
    def __init__(self,position):
        self.position = position
        self.points = 0
        self.starterArea = 0
        if position == 1:
            self.characters = gameGUI.player1Chars
            self.enemyIndex = 2
        else:
            self.characters = gameGUI.player2Chars
            self.enemyIndex = 1

        if players[self.enemyIndex].starterArea == 0:
            self.starerArea = input('which starting area will you chose: 1-4')
        elif players[1].starterArea == 1 or players[1].startArea == 2:
            self.starerArea = input('choose between the two starter areas on the right: 3-4')
        else:
            self.starerArea = input('choose between the two starter areas on the left: 1-2')

    def playerCharactersMove(self):
        numberDead = 0
        for i in self.characters:
            if i.attackVal == 'KO':
                numberDead += 1
                next(self.characters)

            position = 0
            enemyTarget = self.chooseTarget(i)
            self.move(i,position,enemyTarget)
            self.attack(i,enemyTarget)
        if numberDead == 3:
            admitDefeat(self.position,self.points)

    # move and attack are in player class because only the player should move their pieces
    def move(self,character,start,end):
        moveLimit = self.characters[character].speedVal
        finalPosition = Pathing.AStarAlgo(start,end,moveLimit,gameGUI.board)
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

    # Decides which target a character should move towards and attack
    def chooseTarget(self,character):

        health = 0
        distance = 0


        return 'hi'

    # Decides if a character should even move or attack this turn
    def characterActions(self,character):
        decisions = {'move' : False, 'attack':False,}
        return decisions
    
# not sure if getChar is needed anymore
def getChar():
    return 'hi'

def admitDefeat(loser,points):
    winner = players[loser.enemyIndex]
    print('player' + str(loser.position) + 'has lost the game while only getting ' + str(loser.points)+ 'points.'
          'Player ' + str(loser.enemyIndex) + 'has won the game with 300 points')


# goes to the next player, I dont think we need a nextTurn methong since there isnt really turns
def nextPlayer():
    if currentPlayer == 1:
        currentPlayer += 1
    if currentPlayer == 2:
        currentPlayer -= 1
    #Do something about resetting the tokens on their characters if they didnt do anything

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
    inputed = int(input('who will go first'))
    while inputed != 1 or inputed != 2:
        if inputed == 1 or inputed == 2:
            currentPlayer = inputed
        else:
            inputed = int(input("please enter a valid number IE 1 or 2"))

    print(player1.characters)
    print(player2.characters)

if __name__ == '__main__':
    main()
