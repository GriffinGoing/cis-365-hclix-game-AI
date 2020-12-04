from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import simpledialog
sys.path.append('..')
import board
from board import directions
from characterGUI import *
import game

# REQUIRE PYTHON 3.5
def requireVersion():
    if (sys.version_info[0] != 3):
        print("This script requires Python version 3.x")
        sys.exit(1)

class boardButton(Button):
    def __init__(self):
        self.stuff = 0
        self.highlightcolor = 'pale green'


    def highlight(self):
        self.highlightcolor = 'pale green'



class boardGUI:
    count = 0

    def __init__(self, master, board):
        self.count = 0
        self.master = master
        #master.title("HeroClix Interface")

        self.blackBoxes = []
        self.buttons = {}

        self.numRows = 16
        self.numCols = 16

        #self.label = Label(master, text="The Big Boy H-Clix GUI")
        #self.label.pack()

        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack()



        for row in range(self.numRows):
            for col in range(self.numCols):
                node = board[col][row]
                newButton = Button(master,text=(node.name.upper()), justify=CENTER, width = 5, height=2)

                if(node.terrain == "normal"):
                    newButton.config(bg='white')
                elif (node.terrain == "water"):
                    newButton.config(bg='blue')
                elif (node.terrain == "start"):
                    newButton.config(bg='tomato')
                elif (node.terrain == "block"):
                    newButton.config(bg='brown')

                #newButton.bind("<Enter>", onHover)
                #newButton.bind("<Leave>", exitHover)
                self.buttons[node.name] = newButton
                newButton.grid(row=row, column=col, padx=2, pady=2)


    def addWalls(self,board, canvas):
        canvas.update()
        nodeHeight = canvas.winfo_height()/16
        nodeWidth = canvas.winfo_width()/16
        for r in range(16):
            for c in range(16):
                node = board[r][c]
                startX = r*nodeWidth
                startY = c*nodeHeight

                if node.walls[directions.NORTH] == True:
                    canvas.create_line(startX,startY,startX + nodeWidth,startY,width=6)
                if node.walls[directions.EAST] == True:
                    canvas.create_line(startX+nodeWidth,startY,startX + nodeWidth,startY+nodeHeight,width=6)
                if node.walls[directions.SOUTH] == True:
                    canvas.create_line(startX,startY+nodeHeight,startX + nodeWidth,startY+nodeHeight,width=6)
                if node.walls[directions.WEST] == True:
                    canvas.create_line(startX,startY,startX,startY+nodeHeight,width=6)


    def removeWalls(self, nodeEntry, directionEntry, canvas, board):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

        node = nodeEntry.get().lower()
        direction = directionEntry.get().lower()

        prompt = "Remove " + direction.upper() + " wall at " + node.upper() + " ?"

        answer = messagebox.askyesno("Remove Wall?", prompt)

        if (answer == False):
            return

        #print(node)
        #print(direction)

        col = letters.index(node[0])
        row = int(node[1:]) - 1

        #print(row, col)
        canvas.update()
        board.removeWall(col, row, direction)
        nodeHeight = canvas.winfo_height() / 16
        nodeWidth = canvas.winfo_width() / 16
        startX = col * nodeWidth
        startY = row * nodeHeight
        node = board.graph[col][row]
        if node.walls[directions.NORTH] == False:
            canvas.create_line(startX, startY, startX + nodeWidth, startY, width=6, fill='white')
        if node.walls[directions.EAST] == False:
            canvas.create_line(startX + nodeWidth, startY, startX + nodeWidth, startY + nodeHeight, width=6, fill='white')
        if node.walls[directions.SOUTH] == False:
            canvas.create_line(startX, startY + nodeHeight, startX + nodeWidth, startY + nodeHeight, width=6, fill='white')
        if node.walls[directions.WEST] == False:
            canvas.create_line(startX, startY, startX, startY + nodeHeight, width=6, fill='white')




def moveCharacter(character, boardGui):


    # update actual char position
    charName = character.getCharacter()['name']
    oldPosition = character.getCharacter()['position'].lower()
    newPosition = simpledialog.askstring("Move Character", "Enter the position to move " + charName + " to").lower()
    print("Moving " + charName + " to " + newPosition)

    boardGui.buttons[oldPosition].config(image='', width=5, height=2)

    # add new image to board
    width = boardGui.buttons[newPosition].winfo_width()
    height = boardGui.buttons[newPosition].winfo_height()
    print(boardGui.buttons[newPosition].winfo_width(), boardGui.buttons[newPosition].winfo_height())
    boardGui.buttons[newPosition].config(image=character.getCharacter()['thumbnail'], width=width-6, height=height-6)
    print(boardGui.buttons[newPosition].winfo_width(), boardGui.buttons[newPosition].winfo_height())

    # set char position
    character.setPosition(newPosition)

def main():

    root = Tk()

    board.main()

    #root.minsize(1600, 1300)

    font = tkFont.Font(family="Helvetica",size=8)
    root.option_add("*Font", font)
    root.title("HeroClix AI Interface")

    boardFrame = Frame(root)

    aiButtonFrame = Frame(boardFrame)

    nextMoveButton = Button(aiButtonFrame, text="Get Next Move", width=15, height=4, bg="lawn green")
    nextMoveButton.grid(row=0, column=0)

    nodeLabel = Label(aiButtonFrame, text="Node:")
    nodeLabel.grid(row=0, column=1)

    nodeEntry = Entry(aiButtonFrame)
    nodeEntry.grid(row=0, column=2)

    directionLabel = Label(aiButtonFrame, text="Direction:")
    directionLabel.grid(row=0, column=3)

    directionEntry = ttk.Combobox(aiButtonFrame, values=("north", "east", "south", "west"))
    directionEntry.grid(row=0,column=4)

    destroyWallButton = Button(aiButtonFrame, text="Destroy Wall", width=15, height=4, bg="orange")
    destroyWallButton.grid(row=0, column=5)

    canvas = Canvas(boardFrame, bg='white', height=300, width=300) # background or board
    player1LabelFrame = LabelFrame(root, text="Player 1", width=300)
    player2LabelFrame = LabelFrame(root, text="Player 2", width=300)
    player1LabelFrame.grid_propagate(0)

    my_gui = boardGUI(canvas, board.graph)

    destroyWallButton.config(command= lambda nodeEntry=nodeEntry, directionEntry=directionEntry, canvas=canvas, board=board : my_gui.removeWalls(nodeEntry, directionEntry, canvas, board))

    p1CaptAmerica = characterGUI(player1LabelFrame, 1, "Captain America",)
    p1CaptAmerica.moveButton.config(command=lambda character=p1CaptAmerica, boardGui=my_gui : moveCharacter(character, boardGui))

    p1Thor = characterGUI(player1LabelFrame, 1, "Thor",)
    p1Thor.moveButton.config(command=lambda character=p1Thor, boardGui=my_gui : moveCharacter(character, boardGui))

    p1IronMan = characterGUI(player1LabelFrame, 1, "Iron Man",)
    p1IronMan.moveButton.config(command=lambda character=p1IronMan, boardGui=my_gui : moveCharacter(character, boardGui))

    player1Chars = {
        "Captain America": p1CaptAmerica,
        "Thor": p1Thor,
        "Iron Man": p1IronMan
    }

    p2CaptAmerica = characterGUI(player2LabelFrame, 2, "Captain America",)
    p2CaptAmerica.moveButton.config(command=lambda character=p2CaptAmerica, boardGui=my_gui : moveCharacter(character, boardGui))

    p2Thor = characterGUI(player2LabelFrame, 2, "Thor",)
    p2Thor.moveButton.config(command=lambda character=p2Thor, boardGui=my_gui : moveCharacter(character, boardGui))

    p2IronMan = characterGUI(player2LabelFrame, 2, "Iron Man",)
    p2IronMan.moveButton.config(command=lambda character=p2IronMan, boardGui=my_gui : moveCharacter(character, boardGui))

    player2Chars = {
        "Captain America": p2CaptAmerica,
        "Thor": p2Thor,
        "Iron Man": p2IronMan
    }

    player1LabelFrame.grid(row=0,column=0)
    #testp1Label.pack()
    player2LabelFrame.grid(row=0,column=2)
    #testp2Label.pack()
    aiButtonFrame.pack()
    canvas.pack()
    boardFrame.grid(row=0, column=1)
    my_gui.addWalls(board.graph, canvas)

    p2CaptAmerica.setPosition('n1')
    p2IronMan.setPosition('n2')
    p2Thor.setPosition('n3')
    p1IronMan.setPosition('c2')
    p1CaptAmerica.setPosition('c3')
    p1Thor.setPosition('c1')
    game.main(player1Chars,player2Chars)
    nextMoveButton.config(command = lambda p1Chars=player1Chars, p2Chars=player2Chars, board=board.graph : game.nextTurn(p1Chars, p2Chars, board))

    root.mainloop()
    #player1Window.mainloop()


if __name__ =="__main__":
    main()
