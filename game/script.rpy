# The script of the game goes in this file.
# The game starts here.

label start:
    
    # Ask for player name
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()  # Strip whitespace from the input

    # Ensure player_name is not empty
    if player_name == "":
        $ player_name = "Player"

    # Create a new player object dynamically
    $ player = Player(Character, player_name)

    # Print the player's name
    "Hello, [player.name]!"

    jump introduction

label introduction:
    # Intro sequence
    jump gameplay

label gameplay:
    jump renault_route # Placeholder

label renault_route:

    jump end_sequence

label crane_route:
    
    jump end_sequence

label ephraim_route:
    
    jump end_sequence

label end_sequence:


