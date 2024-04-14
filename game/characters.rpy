# Characters are defined here

# This block of python code runs when the game first initializes
init python: 
    import renpy.exports as renpy
    # Enable logging for debugging
    import logging
    logger = logging.getLogger("game")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    class Actor:
        # must pass in (self, Character) at minimum
        def __init__(self, Character, name, affection):
            self.character = Character
            self.name = name
            self._affection = affection # private attribute (_ is naming convention for private attribute)
            logger.debug(f"Actor initialized: {self.name} with affection {self._affection}")
        
        @property
        def affection(self):
            """Gets the actor's affection level."""
            return self._affection
        
        @affection.setter
        def affection(self, value):
            """Sets the actor's affection level, ensuring it stays within a 0-100 range."""
            try:
                if not isinstance(value, int):
                    raise ValueError("Affection must be an integer")
                self._affection = max(min(value, 100), 0)  # Enforce range within 0-100
                logger.debug(f"Set affection for {self.name} to {self._affection}")
            except Exception as e:
                logger.error(f"Error setting affection for {self.name}: {e}")
                raise
            
        def affection_up(self, amount):
            try:
                if not isinstance(amount, int):
                    raise ValueError("Amount must be an integer")
                self.affection += amount
                renpy.notify(f"{self.name} affection up")
                logger.debug(f"Increased affection for {self.name} by {amount}")
            except Exception as e:
                logger.error(f"Error increasing affection for {self.name}: {e}")
            
        def affection_down(self, amount):
            try:
                if not isinstance(amount, int):
                    raise ValueError("Amount must be an integer")
                self.affection -= amount
                renpy.notify(f"{self.name} affection down" )
                logger.debug(f"Decreased affection for {self.name} by {amount}")
            except Exception as e:
                logger.error(f"Error decreasing affection for {self.name}: {e}")
            

    class Player:
        def __init__(self, Character, name):
            self.character = Character
            self.name = name
            logger.debug(f"Player initialized: {self.name}")

        @property
        def name(self):
            """Gets the player's name."""
            return self._name
            
        @name.setter
        def name(self, value):
            """Sets the player's name."""
            try:
                if not isinstance(value, str) or not value:
                    raise ValueError("Name must be a non-empty string")
                self._name = value
                logger.debug(f"Set player name to {self._name}")
            except Exception as e:
                logger.error(f"Error setting player name: {e}")
                raise

# define e = Character("Eileen", color = "#FFFFFF", image="eileen")

define e = Actor(Character("Eileen", color = "#FFFFFF", image="eileen"),"Eileen", 0)

# characters are initialized at the start of the game, player character will be initialized dynamically in script.rpy due to its dynamic nature (custom name input)
define renault = Actor(Character("Renault", color = "#0000FF", image="renault"), "Renault", 0)
define crane = Actor(Character("Crane", color = "#FFFF00", image="crane"), "Crane", 0)
define ephraim = Actor(Character("Ephraim", color = "#FFFFFF"), "Ephraim", 0)
