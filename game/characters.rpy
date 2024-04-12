# Characters are defined here

# This block of python code runs when the game first initializes
init python: 
    class Actor:
        # must pass in (self, Character) at minimum
        def __init__(self, Character, name, affection):
            self.c = Character
            self.name = name
            self._affection = affection # private attribute (_ is naming convention for private attribute)
        
        @property
        def affection(self):
            """Gets the actor's affection level."""
            return self._affection
        
        @affection.setter
        def affection(self, value):
            """Sets the actor's affection level, ensuring it stays within a 0-100 range."""
            if not isinstance(value, int):
                raise ValueError("Affection must be an integer")
            self._affection = max(min(value, 100), 0)  # Enforce range within 0-100
            
        def affection_up(self, amount):
            if not isinstance(amount, int):
                raise ValueError("Amount must be an integer")
            self.affection += amount
            renpy.notify(f"{self.name} affection up")
            
        def affection_down(self, amount):
            if not isinstance(amount, int):
                raise ValueError("Amount must be an integer")
            self.affection -= amount
            renpy.notify(f"{self.name} affection down" )
            

    class Player:
        def __init__(self, Character, name):
            self.c = Character
            self.name = name

        @property
        def name(self):
            """Gets the player's name."""
            return self._name
            
        @name.setter
        def name(self, value):
            """Sets the player's name."""
            if not isinstance(value, str) or not value:
                raise ValueError("Name must be a non-empty string")
            self._name = value

# define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define e = Actor(Character("Eileen", color = "#FFFFFF", image="eileen"),"Eileen", 0)

# characters are initialized at the start of the game, player character will be initialized dynamically in script.rpy due to its dynamic nature (custom name input)
define renault = Actor(Character("Renault"), "Renault", 0)
define crane = Actor(Character("Crane"), "Crane", 0)
define ephraim = Actor(Character("Ephraim"), "Ephraim", 0)
