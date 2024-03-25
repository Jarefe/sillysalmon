# Characters are defined here

init python: # This block of python code runs when the game first initializes
    class Actor:
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self.affection = 


define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define player = Character("[player_name]")