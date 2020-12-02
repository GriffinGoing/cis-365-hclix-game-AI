from tkinter import *
import tkinter.font as tkFont
sys.path.append('..')
import board
from board import directions
from characterGUI import *

# REQUIRE PYTHON 3.5
def requireVersion():
    if (sys.version_info[0] != 3):
        print("This script requires Python version 3.x")
        sys.exit(1)

board = board.main()

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
        self.buttons = []

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
                newButton = Button(master,text=(node.name.upper()), highlightcolor='pale green', justify=CENTER, width = 5, height=2)

                if(node.terrain == "normal"):
                    newButton.config(bg='white')
                elif (node.terrain == "water"):
                    newButton.config(bg='blue')
                elif (node.terrain == "start"):
                    newButton.config(bg='tomato')

                newButton.bind("<Enter>", onHover)
                newButton.bind("<Leave>", exitHover)
                self.buttons.append(newButton)
                newButton.grid(row=row, column=col, padx=2, pady=2)


    def addWalls(self,board):
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


def onHover(event):
    widget = event.widget
    text = str(widget.cget('text')).lower()
    node = board[ord(text[0]) - 97][int(text[1:len(text)]) - 1]
    for i in my_gui.buttons:
        iText = str(i.cget('text')).lower()
        coordx = ord(iText[0]) - 97
        coordy = int(iText[1:len(text)]) - 1
        tempNode = board[coordx][coordy]
        if node.adjacentTo.count(tempNode) == 1:
            i.config(bg='pale green')
    widget.configure(bg='green')

def exitHover(event):
    widget = event.widget
    text = str(widget.cget('text')).lower()
    node = board[ord(text[0]) - 97][int(text[1:len(text)]) - 1]
    for i in my_gui.buttons:
        iText = str(i.cget('text')).lower()
        coordx = ord(iText[0]) - 97
        coordy = int(iText[1:len(text)]) - 1
        tempNode = board[coordx][coordy]
        if node.adjacentTo.count(tempNode) == 1:
            if (tempNode.terrain == "water"):
                i.config(bg='blue')
            elif (tempNode.terrain == "start"):
                i.config(bg='tomato')
            else:
                i.config(bg= 'white')
    if (node.terrain == "water"):
        widget.config(bg='blue')
    elif (node.terrain == "start"):
        widget.config(bg='tomato')
    else:
        i.config(bg='white')



root = Tk()


font = tkFont.Font(family="Helvetica",size=11)
root.option_add("*Font", font)
root.title("HeroClix AI Interface")

canvas = Canvas(root, bg='white', height=300, width=300) # background or board
player1LabelFrame = LabelFrame(root, text="Player 1")
player2LabelFrame = LabelFrame(root, text="Player 2")

my_gui = boardGUI(canvas, board)

# testing
testp1Label = Label(player1LabelFrame, text="IM A TEST SHIT THING")
testp2Label = Label(player2LabelFrame, text="IM A TEST SHIT THING")

p1CaptAmerica = characterGUI(player1LabelFrame, 1, "Captain America",)
p1Thor = characterGUI(player1LabelFrame, 1, "Thor",)
p1IronMan = characterGUI(player1LabelFrame, 1, "Iron Man",)

player1Chars = {
    "Captain America": p1CaptAmerica,
    "Thor": p1Thor,
    "Iron Man": p1IronMan
}

p2CaptAmerica = characterGUI(player2LabelFrame, 2, "Captain America",)
p2Thor = characterGUI(player2LabelFrame, 2, "Thor",)
p2IronMan = characterGUI(player2LabelFrame, 2, "Iron Man",)

player2Chars = {
    "Captain America": p2CaptAmerica,
    "Thor": p2Thor,
    "Iron Man": p2IronMan
}



player1LabelFrame.grid(row=0,column=0)
#testp1Label.pack()
player2LabelFrame.grid(row=0,column=2)
#testp2Label.pack()
canvas.grid(row=0, column=1)
my_gui.addWalls(board)


root.mainloop()
#player1Window.mainloop()