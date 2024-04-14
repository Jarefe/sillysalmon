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
    "pick your route" 
    menu:
        "renault":
            jump renault_route
        "crane":
            jump crane_route
        "ephraim":
            jump ephraim_route


label renault_route:
    show renault
    renault.character "hello"
    jump end_sequence

label crane_route:
    transform crane_half_size:
        zoom 0.5
    show crane at crane_half_size
    crane.character "hello"
    jump end_sequence

label ephraim_route:
    "not yet implemented"
    jump end_sequence

label end_sequence:


