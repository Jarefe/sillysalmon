# Characters are defined here

init python: 
    class Actor:
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self.affection = affection


define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define player = Character("[player_name]")