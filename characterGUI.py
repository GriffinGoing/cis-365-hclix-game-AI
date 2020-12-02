from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

'''
Character attributes/abilities/image/etc
'''

captAmericaTemplate = {
    "name": "Captain America",
    "image": {
        1: "./images/p1CaptainAmerica.jpg",
        2: "./images/p2CaptainAmerica.jpg",
    },
    "keywords": ["Avengers", "S.H.I.E.L.D.", "Solder"],
    "canFly": False,
    "life": 6,
    "deadAt": 7,
    "special": "Shield Up!",
    "speedVals": {
        **dict.fromkeys([1], 8),
        **dict.fromkeys([2, 3], 7),
        **dict.fromkeys([4, 5], 6),
        **dict.fromkeys([6], 5),
        **dict.fromkeys([7], "KO")
    },
    "speedAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Charge"),
        **dict.fromkeys([4, 5, 6], "Sidestep"),
        **dict.fromkeys([7], "**")
    },
    "attackVals": {
        **dict.fromkeys([1], 11),
        **dict.fromkeys([2, 3], 10),
        **dict.fromkeys([4, 5, 6], 9),
        **dict.fromkeys([7], "KO")
    },
    "attackAbilityVals": {
        **dict.fromkeys([1, 2, 3, 4, 5, 6], "None"),
        **dict.fromkeys([7], "**")

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
    "defenseAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Combat Reflexes"),
        **dict.fromkeys([4, 5, 6], "Willpower"),
        **dict.fromkeys([7], "**")
    },
    "damageVals": {
        **dict.fromkeys([1, 2, 3], 3),
        **dict.fromkeys([4, 5, 6], 2),
        **dict.fromkeys([7], "KO")
    },
    "damageAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Leadership"),
        **dict.fromkeys([4, 5, 6], "Close Combat Expert"),
        **dict.fromkeys([7], "**")
    },

}

thorTemplate = {
    "name": "Thor",
    "image": {
        1: "./images/p1Thor.jpg",
        2: "./images/p2Thor.jpg",
    },
    "keywords": ["Avengers", "Asgardian", "Deity"],
    "canFly": True,
    "life": 9,
    "deadAt": 10,
    "special": "Quake",
    "speedVals": {
        **dict.fromkeys([1, 2, 3, 4, 5, 6], 10),
        **dict.fromkeys([7, 8, 9], 9),
        **dict.fromkeys([10], "KO")
    },
    "speedAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Charge"),
        **dict.fromkeys([4, 5, 6], "Running Shot"),
        **dict.fromkeys([7, 8, 9], "Sidestep"),
        **dict.fromkeys([10], "**")
    },
    "attackVals": {
        **dict.fromkeys([1, 2, 3], 11),
        **dict.fromkeys([4, 5, 6], 10),
        **dict.fromkeys([7, 8, 9], 9),
        **dict.fromkeys([10], "KO")
    },
    "attackAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Super Strength"),
        **dict.fromkeys([4, 5, 6], "Energy Explosion"),
        **dict.fromkeys([7, 8, 9], "Special"),
        **dict.fromkeys([10], "**")
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
    "defenseAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Impervious"),
        **dict.fromkeys([4, 5, 6], "Invulnerability"),
        **dict.fromkeys([7, 8, 9], "Willpower"),
        **dict.fromkeys([10], "**")
    },
    "damageVals": {
        **dict.fromkeys([1, 2], 4),
        **dict.fromkeys([3, 4, 5, 6, 7, 8, 9], 3),
        **dict.fromkeys([10], "KO")
    },
    "damageAbilityVals": {
        **dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9], "None"),
        **dict.fromkeys([10], "**")
    },
}

ironManTemplate = {
    "name": "Iron Man",
    "image": {
        1: "./images/p1IronMan.jpg",
        2: "./images/p2IronMan.jpg",
    },
    "keywords": ["Avengers", "Stark Industries", "Armor"],
    "canFly": True,
    "life": 7,
    "deadAt": 8,
    "special": "None",
    "speedVals": {
        **dict.fromkeys([1, 2, 3], 10),
        **dict.fromkeys([4, 5], 9),
        **dict.fromkeys([6, 7], 8),
        **dict.fromkeys([8], "KO")
    },
    "speedAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Running Shot"),
        **dict.fromkeys([4, 5, 6, 7], "Sidestep"),
        **dict.fromkeys([8], "**")
    },
    "attackVals": {
        **dict.fromkeys([1, 2, 3], 10),
        **dict.fromkeys([4, 5, 6, 7], 9),
        **dict.fromkeys([8], "KO")
    },
    "attackAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Energy Explosion"),
        **dict.fromkeys([4, 5, 6, 7], "None"),
        **dict.fromkeys([8], "**")
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
    "defenseAbilityVals": {
        **dict.fromkeys([1, 2, 3], "Invulnerability"),
        **dict.fromkeys([4, 5, 6, 7], "Toughness"),
        **dict.fromkeys([8], "**")
    },
    "damageVals": {
        **dict.fromkeys([1], 4),
        **dict.fromkeys([2, 3], 3),
        **dict.fromkeys([4, 5, 6, 7], 2),
        **dict.fromkeys([8], "KO")
    },
    "damageAbilityVals": {
        **dict.fromkeys([1, 2, 3], "None"),
        **dict.fromkeys([4, 5, 6, 7], "Ranged Combat Expert"),
        **dict.fromkeys([8], "**")
    },
}

characters = {
    "Captain America": captAmericaTemplate,
    "Thor": thorTemplate,
    "Iron Man": ironManTemplate
}

class characterGUI():
    def __init__(self, master, playerNum, character):
        # copy character template
        self.character = characters[character].copy()

        # load proper image
        self.character['image'] = self.character['image'][playerNum]

        # add 'current' attribute keys and values to character
        self.character['speed'] = self.character['speedVals'][1]
        self.character['attack'] = self.character['attackVals'][1]
        self.character['range'] = self.character['rangeVals'][1]
        self.character['defense'] = self.character['defenseVals'][1]
        self.character['damage'] = self.character['damageVals'][1]

        # add current abilities
        self.character['speedAbility'] = self.character['speedAbilityVals'][1]
        self.character['attackAbility'] = self.character['attackAbilityVals'][1]
        self.character['defenseAbility'] = self.character['defenseAbilityVals'][1]
        self.character['damageAbility'] = self.character['damageAbilityVals'][1]


        # named frame to hold char interface
        self.charLabelFrame = LabelFrame(master, text=self.character['name'])

        # frame to pic and name
        self.picFrame = Frame(self.charLabelFrame)

        # frame for clicker
        self.clickerFrame = Frame(self.charLabelFrame)

        # pack keywords in between

        # frame to hold char vals/abilities
        self.attrFrame = Frame(self.charLabelFrame, width=260, height=110)
        self.attrFrame.grid_propagate(False)

        # load and size char image
        self.charImg = ImageTk.PhotoImage(Image.open(self.character['image']).resize((100, 100)), Image.ANTIALIAS)
        self.image = Label(self.picFrame, image=self.charImg)

        # character name
        self.nameLabel = Label(self.picFrame, text=self.character['name'])

        #self.traitLabel = Label(self.charLabelFrame, text="Traits:")
        self.traitVal = Label(self.charLabelFrame, text=", ".join(self.character['keywords']))

        # scale/slider for selection of "clicker" value
        self.clickerLabel = Label(self.clickerFrame, text="Clicker Position:")
        self.clickerSlider = Scale(self.clickerFrame, from_=1, to=self.character['deadAt'], orient=HORIZONTAL, command=self.updateDisplay)

        # ability label
        self.speedAbilityLabel = Label(self.attrFrame, text="Ability:")
        self.attackAbilityLabel = Label(self.attrFrame, text="Ability:")
        self.defenseAbilityLabel = Label(self.attrFrame, text="Ability:")
        self.damageAbilityLabel = Label(self.attrFrame, text="Ability:")

        # speed vals
        self.speedLabel = Label(self.attrFrame, text="Speed:")
        self.speedVal = Label(self.attrFrame, text=self.character['speed'])
        self.speedAbilityVal = Label(self.attrFrame, text=self.character['speedAbility'])

        # attack vals
        self.attackLabel = Label(self.attrFrame, text="Attack:")
        self.attackVal = Label(self.attrFrame, text=self.character['attack'])
        self.attackAbilityVal = Label(self.attrFrame, text=self.character['attackAbility'])


        # range vals
        self.rangeLabel = Label(self.attrFrame, text="Range:")
        self.rangeVal = Label(self.attrFrame, text=self.character['range'])

        # defense vals
        self.defenseLabel = Label(self.attrFrame, text="Defense:")
        self.defenseVal = Label(self.attrFrame, text=self.character['defense'])
        self.defenseAbilityVal = Label(self.attrFrame, text=self.character['defenseAbility'])

        # damage vals
        self.damageLabel = Label(self.attrFrame, text="Damage:")
        self.damageVal = Label(self.attrFrame, text=self.character['damage'])
        self.damageAbilityVal = Label(self.attrFrame, text=self.character['damageAbility'])


        # special ability
        self.specialLabel = Label(self.attrFrame, text="Special:")
        self.specialVal = Label(self.attrFrame, text=self.character['special'])

        self.nameLabel.grid(row=0, column=1)
        self.image.grid(row=0, column=0)

        self.clickerLabel.grid(row=0, column=0)
        self.clickerSlider.grid(row=0, column=1)

        self.speedLabel.grid(row=0, column=0)
        self.speedVal.grid(row=0, column=1)
        self.speedAbilityLabel.grid(row=0, column=2)
        self.speedAbilityVal.grid(row=0, column=3)

        self.attackLabel.grid(row=1, column=0)
        self.attackVal.grid(row=1, column=1)
        self.attackAbilityLabel.grid(row=1, column=2)
        self.attackAbilityVal.grid(row=1, column=3)

        self.rangeLabel.grid(row=2, column=0)
        self.rangeVal.grid(row=2, column=1)

        self.defenseLabel.grid(row=3, column=0)
        self.defenseVal.grid(row=3, column=1)
        self.defenseAbilityLabel.grid(row=3, column=2)
        self.defenseAbilityVal.grid(row=3, column=3)

        self.damageLabel.grid(row=4, column=0)
        self.damageVal.grid(row=4, column=1)
        self.damageAbilityLabel.grid(row=4, column=2)
        self.damageAbilityVal.grid(row=4, column=3)

        self.specialLabel.grid(row=5, column=0)
        self.specialVal.grid(row=5, column=1)

        self.picFrame.pack()
        self.traitVal.pack()
        self.clickerFrame.pack()
        self.attrFrame.pack()
        #self.attrFrame.grid_propagate(0)

        print(self.attrFrame.winfo_width(), self.attrFrame.winfo_height())

        self.charLabelFrame.pack()


    def updateDisplay(self, val):
        #print(self.character['speed']) # just a test

        # update visual speeds
        self.character['speed'] = self.character['speedVals'][int(val)]
        self.character['attack'] = self.character['attackVals'][int(val)]
        self.character['range'] = self.character['rangeVals'][int(val)]
        self.character['defense'] = self.character['defenseVals'][int(val)]
        self.character['damage'] = self.character['damageVals'][int(val)]

        # update visual attrs
        self.character['speedAbility'] = self.character['speedAbilityVals'][int(val)]
        self.character['attackAbility'] = self.character['attackAbilityVals'][int(val)]
        self.character['defenseAbility'] = self.character['defenseAbilityVals'][int(val)]
        self.character['damageAbility'] = self.character['damageAbilityVals'][int(val)]


        # update visual speeds
        self.speedVal.config(text=self.character['speed'])
        self.attackVal.config(text=self.character['attack'])
        self.rangeVal.config(text=self.character['range'])
        self.defenseVal.config(text=self.character['defense'])
        self.damageVal.config(text=self.character['damage'])

        self.speedAbilityVal.config(text=self.character['speedAbility'])
        self.attackAbilityVal.config(text=self.character['attackAbility'])
        self.defenseAbilityVal.config(text=self.character['defenseAbility'])
        self.damageAbilityVal.config(text=self.character['damageAbility'])


    def getCharacter(self):
        return self.character


