# The script of the game goes in this file.
# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen vhappy

    # These display lines of dialogue.

    e.c "You've created a new Ren'Py game." 

    e.c "Once you add a story, pictures, and music, you can release it to the world!"

    # Ask for player name
    # $ means following line is a python snippet
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    e.c "Nice to meet you, [player_name]!"

    # This is how to implement choice menus with flags

    label choices:
        default flag = False
        e "Yes or no?"
    menu:
        "Yes":
            jump choices1_a
        "No":
            jump choices1_b

    label choices1_a:
        e.c "You selected yes and flag is set to true"
        $ flag = True
        jump choices1_common
    
    label choices1_b:
        e.c "You selected no and flag remains false"
        $ flag = False
        jump choices1_common

    label choices1_common:
        e.c "This is text that follows the choice related dialogue"

    # This is how to implement flags

    label flags:
        if flag:
            "This is text that displays when you triggered the flag"
        else:
            "This is text that displays when the flag has not been triggered"

    
    # The following block is an example of how to implement flags to determine routes

    label romance_choices:
        e.c "First or second?"
        menu:
            "First":
                e "Correct"
                $ eileen_affection += 1
                "Affection value has risen by 1"
            "Second":
                e "Incorrect"
        e "Red or blue?"
        menu:
            "Red":
                e "Correct"
                $ eileen_affection += 1
                "Affection value has risen by 1"
            "Blue":
                e "Incorrect"
        e "Apple or banana?"
        menu:
            "Apple":
                e "Correct"
                $ eileen_affection += 1
                "Affection value has risen by 1"
            "Banana":
                e "Incorrect"
    
    label ending_evaluation:
        "Current affection value is [eileen_affection]"
        if eileen_affection >= 2:
            jump eileen_good_ending
        elif eileen_affection == 1:
            jump eileen_okay_ending
        else:
            jump eileen_bad_ending

    label eileen_good_ending:
        "You won"
        jump ending_credits
    
    label eileen_okay_ending:
        "Nothing changed"
        jump ending_credits
    
    label eileen_bad_ending:
        "You died"
        jump ending_credits

    label ending_credits:
        "insert credits"

    # This ends the game.

    return
