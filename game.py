import gameGUI
import Pathing
from random import randint
global currentPlayer

class player():
    def __init__(self,position):
        self.position = position
        if position == 1:
            self.characters = gameGUI.player1Chars
        if position == 2:
            self.characters = gameGUI.player2Chars

    #move and attack are in player class because only the player should move their pieces
    def move(self,character,start,end):
        moveLimit = self.characters[character].speedVal
        finalPosition = Pathing.AStarAlgo(start,end,moveLimit,gameGUI.board)
        return 'hi'

    def attack(self):
        return 'hi'

#not sure if getChar is needed anymore
def getChar():
    return 'hi'



#goes to the next player, I dont think we need a nextTurn methong since there isnt really turns
def nextPlayer():
    if currentPlayer == 1:
        currentPlayer += 1
    if currentPlayer == 2:
        currentPlayer -= 1
    #Do something about resetting the tokens on their characters if they didnt do anything

#roll dice
def rollDice(start,end):
    return randint(start,end)

#creates
def main():
    GUI = gameGUI.main()
    player1 = player(1)
    player2 = player(2)
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