# Characters are defined here

# This block of python code runs when the game first initializes
init python: 
    class Actor:
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self.affection = affection
        
        def affection_up(amount):
            self.affection += amount
            renpy.notify("Affection up")
            
        def affection_down(amount):
            self.affection -= amount
            renpy.notify("Affection down")


# define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define e = Actor(Character("Eileen"), "Eileen", 0)

# define player = Character("[player_name]")

