# Characters are defined here

# This block of python code runs when the game first initializes
init python: 
    class Actor:
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self.affection = affection


# define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define e = Actor(Character("Eileen"), "Eileen", 0)

# define player = Character("[player_name]")

define player = 