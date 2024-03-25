# Characters are defined here

# This block of python code runs when the game first initializes
init python: 
    class Actor:
        # must pass in (self, Character) at minimum
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self.affection = affection
        
        def affection_up(amount):
            self.affection += amount
            renpy.notify("Affection up by [amount]")
            
        def affection_down(amount):
            self.affection -= amount
            renpy.notify("Affection down by [amount]")

    class Player:
        def __init__(self, Character, name):
            self.c = Character
            self.name = "Default name"
            
        def change_name(new_name):
            self.name = new_name

# define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define e = Actor(Character("Eileen"), "Eileen", 0)

# define player = Character("[player_name]")

define player = Actor(Character("["default]"), "["default"])
