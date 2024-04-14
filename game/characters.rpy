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
        def __init__(self, Character, name, affection, default_image_tag):
            self.character = Character
            self.name = name
            self._affection = affection # private attribute (_ is naming convention for private attribute)
            self.default_image_tag = default_image_tag
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
        
        def dialogue(self, dialogue_lines, emotion=None, text_speeds=None):
            """
            Displays dialogue for this actor with optional emotion, text speeds, and transform.
            Includes error handling for mismatched text_speeds array length when text speeds are provided.
            If no text speeds are provided, the character's default text speed is used.

            :param dialogue_lines: A list of dialogue lines for the actor.
            :param emotion: An optional emotion to display the character with.
            :param text_speeds: An optional list of text speeds corresponding to each dialogue line.
                                If None, the character's default text speed is used.
            """
            # Error handling for mismatched text_speeds array length
            if text_speeds is not None and len(text_speeds) != len(dialogue_lines):
                logger.error(f"Mismatch in number of text speeds ({len(text_speeds)}) and dialogue lines ({len(dialogue_lines)}) for {self.name}.")
                raise ValueError("Mismatch in number of text speeds and dialogue lines.")

            # TODO: implement transform handling for future potential character animation or alterations

            # Use the default image tag if no emotion is provided
            image_tag = self.default_image_tag if emotion is None else f"{self.name} {emotion}"

            renpy.show(image_tag)

            # Display each line of dialogue with the specified text speed or default if not provided
            for index, line in enumerate(dialogue_lines):
                if text_speeds and index < len(text_speeds) and text_speeds[index] is not None:
                    # Apply the text speed using a text tag at the start of the line if specified
                    line_with_speed = "{cps=%d}%s" % (text_speeds[index], line)
                    renpy.say(self.character, line_with_speed)  # Use self.character for the speaking character
                else:
                    # Use the character's default text speed
                    renpy.say(self.character, line)  # Use self.character for the speaking character

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

# characters are initialized at the start of the game, player character will be initialized dynamically in script.rpy due to its dynamic nature (custom name input)
define renault = Actor(Character("Renault", color = "#0000FF", image="renault", cps=5), "Renault", 0, "renault")
define crane = Actor(Character("Crane", color = "#FFFF00", image="crane", cps=10), "Crane", 0, "crane")
define ephraim = Actor(Character("Ephraim", color = "#FFFFFF", cps=20), "Ephraim", 0, "ephraim")
