# The script of the game goes in this file.
# The game starts here.

label start:

    # NOTE: remove this when finalizing the game
    "The current text speed is [preferences.text_cps]. Remove this message when finalizing"

    python:
        # Ask for player name with error handling and repeat if blank
        player_name = ""
        while player_name.strip() == "":
            try:
                player_name = renpy.input("What is your name?").strip()
                if player_name == "":
                    renpy.say("", "You must enter a name.")
            except Exception as e:
                renpy.say("", "An error occurred. Please try again.")

        # Create a new player object dynamically
        player = Player(Character, player_name)

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
    $ renault.dialogue([
        "hello, my dialogue will show at 5cps by default",
        "this line will show at 10 cps and is changed through the dialogue function",
        "the following line will show variable speeds using the cps tag and is in place as reference for the programmers",
        "{cps=10}Lorem ipsum dolor sit amet{/cps}, {cps=20}consectetur adipiscing elit{/cps}, {cps=30}sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.{/cps}"
    ], text_speeds=[None, 10, None, None])
    jump end_sequence

label crane_route:
    transform crane_half_size:
        zoom 0.5  # Adjust the zoom level as needed to fit the screen
    show crane at crane_half_size
    $ crane.dialogue([
        "hello, my dialogue will show at 10cps by default",
        "this line will show at 20 cps and is changed through the dialogue function",
        "the following line will show variable speeds using the cps tag and is in place as reference for the programmers",
        "{cps=20}Lorem ipsum dolor sit amet{/cps}, {cps=40}consectetur adipiscing elit{/cps}, {cps=60}sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.{/cps}"
    ], text_speeds=[None, 20, None, None])
    jump end_sequence

label ephraim_route:
    $ ephraim.dialogue([
        "hello, my dialogue will show at 20cps by default",
        "this line will show at 40 cps and is changed through the dialogue function",
        "the following line will show variable speeds using the cps tag and is in place as reference for the programmers",
        "{cps=1500}Lorem ipsum dolor sit amet{/cps}, {cps=10}consectetur adipiscing elit{/cps}, {cps=100}sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.{/cps}"
    ], text_speeds=[None, 40, None, None])
    jump end_sequence

label end_sequence:


