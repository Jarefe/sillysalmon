# The script of the game goes in this file.
# The game starts here.

label start:
    
    # Ask for player name
    $ player_name = renpy.input("What is your name?")

    # Create a new player
    $ player = Player(player_name)

    # Print the player's name
    renpy.say(f"Hello, {player.name}!")

    # End the script
    renpy.end_replay()

