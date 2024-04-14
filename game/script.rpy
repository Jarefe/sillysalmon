# The script of the game goes in this file.
# The game starts here.

label start:

    # NOTE: remove this when finalizing the game
    "The current text speed is [preferences.text_cps]. Remove this message when finalizing"

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
    renault.character "hello, my dialogue will show at 5cps"
    renault.character "this is a long line of text that will be split into multiple lines to test how the text will be displayed in the game in addition to checking text speed"
    jump end_sequence

label crane_route:
    transform crane_half_size:
        zoom 0.5
    show crane at crane_half_size
    crane.character "hello, my dialogue will show at 10cps"
    crane.character "this is a long line of text that will be split into multiple lines to test how the text will be displayed in the game in addition to checking text speed"
    jump end_sequence

label ephraim_route:
    ephraim.character "hello, my dialogue will show at 20cps"
    ephraim.character "this is a long line of text that will be split into multiple lines to test how the text will be displayed in the game in addition to checking text speed"
    jump end_sequence

label end_sequence:


