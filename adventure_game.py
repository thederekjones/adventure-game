#!/usr/bin/python3

import time
import random


# Define a length of time to pause as new messages appear on the screen.
def print_pause(message):
    print(message)
    time.sleep(2)


# Introduction to the story for the game itself.
def intro(ancient_artifact, enemy):
    print_pause("You awaken in a dark room with an old,"
                " dirty lamp lit in the corner.")
    print_pause("How did you end up here? The last thing"
                " you remember is being in your bed.")
    print_pause("You slowly stand up and go grab the lamp"
                " so you can get a good look around.")
    print_pause("A desk is situated on the side of the room"
                " with a clean, white piece of paper.")
    print_pause("There is a message written for you. A"
                f" warning? **Beware of the {enemy}!**")
    print_pause("You want to escape. To your left is a door,"
                " and to your right is a window.")


# Ask the user for input to continue the story. If the user provides
# invalid input, it will ask them to enter a valid choice.
def escape(ancient_artifact, enemy):
    print_pause("Press 1 to go through the door.")
    print_pause("Press 2 to go through the window.")

    while True:
        response = input("Where would you like to go?\n")
        if response == "1":
            door(ancient_artifact, enemy)
            break
        elif response == "2":
            window(ancient_artifact, enemy)
            break
        else:
            print_pause("Please enter a valid choice.")
            escape(ancient_artifact, enemy)


# Provides different story output depending on whether or not the user
# has made this selection previously. Returns user to escape() selection.
def door(ancient_artifact, enemy):
    if "blade" in ancient_artifact:
        print_pause("You slowly open the door. The trunk"
                    " is still open with nothing inside.")
        print_pause("You go back into the old bedroom and"
                    " shut the door behind you.")
    else:
        print_pause("You open the door. It appears to be a"
                    " large closet. Inside is a wooden trunk.")
        print_pause("It doesn't seem to be locked. You open"
                    " the trunk and find a note and a blade.")
        print_pause(f"**Behold! THE {enemy.upper()} BLADE!**")
        print_pause("You grab your new weapon and go back to"
                    " the room, closing the door behind you.")
        ancient_artifact.append("blade")
    escape(ancient_artifact, enemy)


# If the user chose to open the door before the window, they will have
# the weapon needed to defeat the enemy, otherwise they will lose. The
# option to start a new game and repeat is available no matter the outcome.
def window(ancient_artifact, enemy):
    print_pause("You go to the window. You're in luck! The"
                " window is unlocked.")
    print_pause("You slide it open and pull yourself through"
                " it carefully.")
    print_pause("You get safely outside when you hear rustling"
                " in the trees.")
    print_pause("Something is coming out of the woods. Oh no!"
                f" It's the {enemy}!")

    if "blade" not in ancient_artifact:
        print_pause(f"The {enemy} is coming toward you and you"
                    " don't have a weapon!")
        print_pause("You fight bravely, but you were no match"
                    " empty handed.")
        print_pause("GAME OVER!")
        new_game()
    else:
        print_pause(f"The {enemy} is coming toward you. You're"
                    " ready for a fight!")
        print_pause("You swing wildly, eventually connecting"
                    f" with the {enemy}.")
        print_pause("It yells out in pain. It falls to the ground"
                    " and turns to dust.")
        print_pause("You've won! A light shines in the distance,"
                    " getting brighter and brighter.")
        print_pause("Eventually all you can see is a bright, white"
                    " light. It has devoured everything.")
        new_game()


# Ask the user whether they want to start a new game or not, and if a
# "yes" or "no" isn't selected, ask the user for valid feedback only.
def new_game():
    print_pause("You wake up... your body covered in sweat.")
    response = input("Would you like to play again? Please"
                     " enter 'yes' or 'no' now.\n").lower()

    if response == "yes":
        print_pause("You've been sprinkled with sleeping dust."
                    " You enter a deep sleep.")
        start_game()
    elif response == "no":
        print_pause("You walk into the kitchen and make some"
                    " coffee. No more sleeping for you!")
        print_pause("THE END!")
    else:
        print_pause("Please enter 'yes' or 'no' only!")
        new_game()


# Randomly select an enemy for the story. The name of the enemy will be
# reflected inside of the name for the weapon. The ancient_artifact array
# starts empty and holds the weapon if found in the story.
def start_game():
    ancient_artifact = []
    enemy = random.choice(["werewolf", "vampire", "skinwalker",
                          "ghoul", "shapeshifter"])

    intro(ancient_artifact, enemy)
    escape(ancient_artifact, enemy)


start_game()
