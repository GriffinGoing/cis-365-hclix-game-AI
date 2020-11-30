from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

'''
Character attributes/abilities/image/etc
'''

captAmericaTemplate = {
    "name": "Captain America",
    "image": "./images/captainAmerica.jpg",
    "keywords": ["Avengers", "S.H.I.E.L.D.", "Solder"],
    "canFly": False,
    "life": 6,
    "deadAt": 7,
    "Special": "Shield Up!",
    "speedVals": {
        **dict.fromkeys([1], 8),
        **dict.fromkeys([2, 3], 7),
        **dict.fromkeys([4, 5], 6),
        **dict.fromkeys([6], 5),
        **dict.fromkeys([7], "KO")
    },
    "attackVals": {
        **dict.fromkeys([1], 11),
        **dict.fromkeys([2, 3], 10),
        **dict.fromkeys([4, 5, 6], 9),
        **dict.fromkeys([7], "KO")
    },
    "rangeVals": {
        **dict.fromkeys([1,2,3,4,5,6], 5),
        **dict.fromkeys([7], "KO")
    },
    "defenseVals": {
        **dict.fromkeys([1, 2, 3], 17),
        **dict.fromkeys([4, 5], 16),
        **dict.fromkeys([6], 17),
        **dict.fromkeys([7], "KO")
    },
    "damageVals": {
        **dict.fromkeys([1, 2, 3], 3),
        **dict.fromkeys([4, 5, 6], 2),
        **dict.fromkeys([7], "KO")
    },

}

thorTemplate = {
    "name": "Thor",
    "image": "./images/thor.jpg",
    "keywords": ["Avengers", "Asgardian", "Deity"],
    "canFly": True,
    "life": 9,
    "deadAt": 10,
    "Special": "Quake",
    "speedVals": {
        **dict.fromkeys([1, 2, 3, 4, 5, 6], 10),
        **dict.fromkeys([7, 8, 9], 9),
        **dict.fromkeys([10], "KO")
    },
    "attackVals": {
        **dict.fromkeys([1, 2, 3], 11),
        **dict.fromkeys([4, 5, 6], 10),
        **dict.fromkeys([7, 8, 9], 9),
        **dict.fromkeys([10], "KO")
    },
    "rangeVals": {
        **dict.fromkeys([1,2,3,4,5,6, 7, 8, 9], 6),
        **dict.fromkeys([10], "KO")
    },
    "defenseVals": {
        **dict.fromkeys([1], 18),
        **dict.fromkeys([2, 3, 4, 5, 6, 7, 8], 17),
        **dict.fromkeys([9], 16),
        **dict.fromkeys([10], "KO")
    },
    "damageVals": {
        **dict.fromkeys([1, 2], 4),
        **dict.fromkeys([3, 4, 5, 6, 7, 8, 9], 3),
        **dict.fromkeys([10], "KO")
    },
}

ironManTemplate = {
    "name": "Iron Man",
    "image": "./images/ironMan.jpg",
    "keywords": ["Avengers", "Stark Industries", "Armor"],
    "canFly": True,
    "life": 7,
    "deadAt": 8,
    "Special": "None",
    "speedVals": {
        **dict.fromkeys([1, 2, 3], 10),
        **dict.fromkeys([4, 5], 9),
        **dict.fromkeys([6, 7], 8),
        **dict.fromkeys([8], "KO")
    },
    "attackVals": {
        **dict.fromkeys([1, 2, 3], 10),
        **dict.fromkeys([4, 5, 6, 7], 9),
        **dict.fromkeys([8], "KO")
    },
    "rangeVals": {
        **dict.fromkeys([1,2,3,4,5,6,7], 7),
        **dict.fromkeys([8], "KO")
    },
    "defenseVals": {
        **dict.fromkeys([1], 18),
        **dict.fromkeys([2, 3, 4, 5], 17),
        **dict.fromkeys([6, 7], 16),
        **dict.fromkeys([8], "KO")
    },
    "damageVals": {
        **dict.fromkeys([1], 4),
        **dict.fromkeys([2, 3], 3),
        **dict.fromkeys([4, 5, 6, 7], 2),
        **dict.fromkeys([8], "KO")
    },
}

characters = {
    "Captain America": captAmericaTemplate,
    "Thor": thorTemplate,
    "Iron Man": ironManTemplate
}

class characterGUI():
    def __init__(self, master, character):
        # copy character template
        self.character = characters[character].copy()

        # add 'current' attribute keys and values to character
        self.character['speed'] = self.character['speedVals'][1]
        self.character['attack'] = self.character['attackVals'][1]
        self.character['range'] = self.character['rangeVals'][1]
        self.character['defense'] = self.character['defenseVals'][1]
        self.character['damage'] = self.character['damageVals'][1]


        # named frame to hold char interface
        self.charLabelFrame = LabelFrame(master, text=self.character['name'])

        # load and size char image
        self.charImg = ImageTk.PhotoImage(Image.open(self.character['image']).resize((100, 100)), Image.ANTIALIAS)
        self.image = Label(self.charLabelFrame, image=self.charImg)

        # character name
        self.nameLabel = Label(self.charLabelFrame, text=self.character['name'])

        # scale/slider for selection of "clicker" value
        self.clickerLabel = Label(self.charLabelFrame, text="Clicker Position:")
        self.clickerSlider = Scale(self.charLabelFrame, from_=1, to=self.character['deadAt'], orient=HORIZONTAL, command=self.updateDisplay)

        # speed vals
        self.speedLabel = Label(self.charLabelFrame, text="Speed:")
        self.speedVal = Label(self.charLabelFrame, text=self.character['speed'])

        # attack vals
        self.attackLabel = Label(self.charLabelFrame, text="Attack:")
        self.attackVal = Label(self.charLabelFrame, text=self.character['attack'])

        # range vals
        self.rangeLabel = Label(self.charLabelFrame, text="Range:")
        self.rangeVal = Label(self.charLabelFrame, text=self.character['range'])

        # defense vals
        self.defenseLabel = Label(self.charLabelFrame, text="Defense:")
        self.defenseVal = Label(self.charLabelFrame, text=self.character['defense'])

        # damage vals
        self.damageLabel = Label(self.charLabelFrame, text="Damage:")
        self.damageVal = Label(self.charLabelFrame, text=self.character['damage'])

        self.nameLabel.grid(row=0, column=1)
        self.image.grid(row=0, column=0)


        self.clickerLabel.grid(row=1, column=0)
        self.clickerSlider.grid(row=1, column=1)

        self.speedLabel.grid(row=2, column=0)
        self.speedVal.grid(row=2, column=1)

        self.attackLabel.grid(row=3, column=0)
        self.attackVal.grid(row=3, column=1)

        self.rangeLabel.grid(row=4, column=0)
        self.rangeVal.grid(row=4, column=1)

        self.defenseLabel.grid(row=5, column=0)
        self.defenseVal.grid(row=5, column=1)

        self.damageLabel.grid(row=6, column=0)
        self.damageVal.grid(row=6, column=1)

        self.charLabelFrame.pack()


    def updateDisplay(self, val):
        #print(self.character['speed']) # just a test

        # update visual speeds
        self.character['speed'] = self.character['speedVals'][int(val)]
        self.character['attack'] = self.character['attackVals'][int(val)]
        self.character['range'] = self.character['rangeVals'][int(val)]
        self.character['defense'] = self.character['defenseVals'][int(val)]
        self.character['damage'] = self.character['damageVals'][int(val)]


        # update visual speeds
        self.speedVal.config(text=self.character['speed'])
        self.attackVal.config(text=self.character['attack'])
        self.rangeVal.config(text=self.character['range'])
        self.defenseVal.config(text=self.character['defense'])
        self.damageVal.config(text=self.character['damage'])


    def getCharacter(self):
        return self.character


