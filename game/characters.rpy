# Characters are defined here

# This block of python code runs when the game first initializes
init python: 
    class Actor:
        # must pass in (self, Character) at minimum
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self.affection = affection
        
        def affection_up(self, amount):
            self.affection += amount
            renpy.notify(f"{self.name} affection up")
            
        def affection_down(self, amount):
            self.affection -= amount
            renpy.notify(f"{self.name} affection down" )
            

    class Player:
        def __init__(self, Character, name):
            self.c = Character
            self.name = "Default name"
            
        def change_name(self, new_name):
            self.name = new_name

# define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define e = Actor(Character("Eileen", color = "#FFFFFF", image="eileen"),"Eileen", 0)

define renault = Actor(Character("Renault"), "Renault", 0)
define crane = Actor(Character("Crane"), "Crane", 0)
define ephraim = Actor(Character("Ephraim"), "Ephraim", 0)

# define player = Character("[player_name]")

define player = Player(Character("[player_name]"), "default")
