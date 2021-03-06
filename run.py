import os
from os import system, name


def clear():
    """
    Clears the screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def begin_game():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    print("\nEli just robbed the Central Bank of the world.")
    print("Eli is trying to escape with large bags of cash.")
    print("The police have been alerted and are in hot pursuit.")
    print("Help Eli escape from the police.")
    print("\nEli storms out of the bank on to the busy road.")
    print("He comes up to a fork at the end of the road.")
    print("He is faced with two choices: ")
    print("\nChoice 1:  Turn left.")
    print("Choice 2:  Turn right.\n")
    while True:
        first_choice = input("What choice do you want to make? ( 1 / 2 ):\n ")
        if first_choice not in ['1', '2']:
            print("That is not a valid option, please try again")
        else:
            if first_choice == '1':
                choice1()
                break
            else:
                choice2()
                break


def restart_eli():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    while True:
        start_eli = input(
            "Would you like to try again? "
            "(Y / N):\n ").lower().strip()
        if start_eli not in ["y", "n"]:
            print("That is not a valid option please try again")
        else:
            if start_eli == 'y':
                begin_game()
                break
            else:
                clear()
                print("Eli won't be getting any help this time")
                print("\nThanks for playing")
                break


def choice1():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    print("\nHe turns left to a narrow path that leads him up to a shed.")
    print("He breaks open the doors to the shed.")
    print("He looks around for anything that can help him escape.")
    print("He finds an open safe that contains three keys: ")
    print("\nChoice 1:  keys to a motorbike.")
    print("Choice 2:  keys to a car.")
    print("Choice 3:  keys to a boat.\n")
    while True:
        second_choice = input("Pick a key ( 1 / 2 / 3 ):\n ")
        if second_choice not in ['1', '2', '3']:
            print("That is not a valid option, please try again")
        else:
            if second_choice == '1':
                choice1_1()
                break
            elif second_choice == '2':
                choice1_2()
                break
            else:
                choice1_3()
                break


def choice1_1():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    print("\nEli takes the keys to the motorbike.")
    print("He starts the motorbike.")
    print("He keeps riding till he comes up to the main road.")
    print("The main road leads to 3 coloured dirt paths:")
    print("\nchoice 1:  The brown dirt path")
    print("choice 2:  The black dirt path")
    print("choice 3:  The grey dirt path\n")
    while True:
        third_choice = input("Choose a dirt path ( 1 / 2 / 3 ):\n ")
        if third_choice not in ['1', '2', '3']:
            print("That is not a valid option, please try again")
        else:
            if third_choice == '1':
                choice1_1a()
                break
            elif third_choice == '2':
                choice1_1b()
                break
            else:
                choice1_1c()
                break


def choice1_1a():
    """
    Prints messages. Provides input method to continu with game.
    Calls another function to restart game.
    """
    clear()
    print(
        "\nAs Eli rides through the brown dirt path, "
        "the motorbike starts to slow down.")
    print(
        "So he stops by a diner in the middle of no where, "
        "only to discover that he is low on fuel.")
    print(
        "He leaves the bike at the diner and continues on foot "
        "through the thick forest behind the diner.")
    print("The police finds his motorbike but cannot find him")
    print("Eli is able escape with all the bags of cash intact.")
    print("Eli is now a very rich man living freely.")
    print("\nCONGRATULATIONS. YOU WIN !!!!!")
    input("\nPress enter to continue")
    restart_eli()


def choice1_1b():
    """
    Prints messages. Provides input method to continue with game.
    Calls another function to restart game.
    """
    clear()
    print("\nAs he rides through the black dirt path, Eli gets to a tunnel.")
    print(
        "Unknown to him there are policemen waiting "
        "on the other side of the tunnel.")
    print(
        "As he gets closer to the other side, the police catch him "
        "by slamming into his motorbike with their cop car")
    print(
        "Eli falls to the ground with all his bags of cash "
        "and the police arrest him.")
    print("\nThat is the end of the road for Eli.")
    input("\nPress enter to continue")
    restart_eli()


def choice1_1c():
    """
    Prints messages. Provides input method to continue with game.
    Calls another function to restart game.
    """
    clear()
    print(
        "\nAs he rides through the grey dirt path, "
        "his bike starts to slow down.")
    print("He discovers that he is low on fuel.")
    print(
        "With no place to stop and refuel, "
        "the bike finally comes to a stop on the road.")
    print("He is now on open land with no cover to hide under.")
    print("The police finally spot him.")
    print("He is arrested and all the stolen cash is recovered.")
    input("\nPress enter to continue")
    restart_eli()


def choice1_2():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    print(
        "\nEli takes the keys to the car,"
        "enters the car and starts driving.")
    print(
        "Not long after he starts driving he hears the police sirens "
        "getting closer and the chase begins. ")
    print(
        "As he drives up the main road, "
        " he comes to a path leading to 2 bridges: ")
    print("\nchoice 1:  Bridge 1")
    print("choice 2:  Bridge 2")
    while True:
        fourth_choice = input("Choose which bridge to take ( 1 / 2 ):\n ")
        if fourth_choice not in ['1', '2']:
            print("That is not a valid option, please try again")
        else:
            if fourth_choice == '1':
                choice1_2a()
                break
            else:
                choice1_2b()
                break


def choice1_2a():
    """
    Prints messages. Provides input method to continue with game.
    Calls another function to restart game.
    """
    clear()
    print(
        "\nAs Eli drives through bridge 1, "
        "the car starts to skid and then overturns.")
    print(
        "He climbs out of the car and starts to run across the bridge, "
        "but the bridge is broken half way.")
    print("The police surrounds him and he is arrested.")
    input("\nPress enter to continue")
    restart_eli()


def choice1_2b():
    """
    Prints messages. Provides input method to continue with game.
    Calls another function to restart game.
    """
    clear()
    print(
        "\nAs Eli drives on to bridge 2, "
        "he sees something at the end of the bridge.")
    print(
        "The end of the bridge has been blocked off "
        "by a broken down fuel tanker.")
    print("He jumps out of the car and makes a run for it.")
    print("He is not fast enough and so the Police catch him.")
    input("\nPress enter to continue")
    restart_eli()


def choice1_3():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    print(
        "\nEli takes the keys to the boat and runs "
        "to the nearby river where he finds the boat parked "
        "and also a scuba gear with an oxygen tank. ")
    print("All he has to do is to choose either: ")
    print("choice 1:  The scuba gear")
    print("choice 2:  The boat")
    while True:
        fifth_choice = input("Which would you like to choose ( 1 / 2 ):\n ")
        if fifth_choice not in ['1', '2']:
            print("That is not a valid option, please try again")
        else:
            if fifth_choice == '1':
                choice1_3a()
                break
            else:
                choice1_3b()
                break


def choice1_3a():
    """
    Prints messages. Provides input method to continue with game.
    Calls another function to restart game.
    """
    clear()
    print("\nEli takes the scuba gear.")
    print("Decides to swim out into the river.")
    print("Unknown to him, there is not enough oxygen in the oxygen tank.")
    print("He drowns after swimming for a few minutes.")
    input("\nPress enter to continue")
    restart_eli()


def choice1_3b():
    """
    Prints messages. Provides input method to continue with game.
    Calls another function to restart game.
    """
    clear()
    print(
        "Eli decides to use the boat but as he moves along the river, "
        "he discovers that there is a  huge hole in the boat. ")
    print("The boat starts to sink very quickly.")
    print(
        "As he does not know how to swim, "
        "he ends up in the river and drowns.")
    input("\nPress enter to continue")
    restart_eli()


def choice2():
    """
    Prints messages. Provides input method for selecting from options.
    Calls other functions based on option selected.
    """
    clear()
    print("\nEli turns right to a wide path that leads up to a house.")
    print("He could either:")
    print("choice 1: Try to break in from the front")
    print("choice 2: Try to break in from the back")
    print("choice 3: Use the hidden key under the door mat\n")
    while True:
        sixth_choice = input("Which choice do you want? ( 1 / 2 / 3 ):\n ")
        if sixth_choice not in ['1', '2', '3']:
            print("That is not a valid option, please try again")
        else:
            clear()
            if sixth_choice == '1':
                print(
                    "He tries to break in from the front, "
                    "but the door is rock solid.")
                print("The police catch up to him and he is arrested.")
                input("\nPress enter to continue")
                restart_eli()
                break
            elif sixth_choice == '2':
                print(
                    "\nHe tries to break in from the back "
                    "by using a large rock to break the window.")
                print(
                    "He climbs into the house to hide, "
                    "but the owner of the house raises an alarm "
                    "which gets the attention of the police near by.")
                print("Eli surrenders.")
                input("\nPress enter to continue")
                restart_eli()
                break
            else:
                print("\nHe uses the hidden key under the mat.")
                print(
                    "He opens the door and makes his way "
                    "into the living room to hide.")
                print("A massive guard dog sees him.")
                print("The dog starts barking and attacks him.")
                print(
                    "Eli screams and tries to fight off the dog, "
                    "but the owner of the house calls the police "
                    "and he is arrested")
                input("\nPress enter to continue")
                restart_eli()
                break


clear()
print("\n\n    #####################")
print("    #                   #")
print("    #  Help Eli Escape  #")
print("    #                   #")
print("    #####################")
print("\n\nEli just robbed the Central Bank of the world.")
print("Eli is trying to escape with large bags of cash.\n")
while True:
    help_eli = input(
        "Would you like to help Eli escape from the police?"
        " (Y / N):\n ").lower().strip()
    if help_eli not in ["y", "n"]:
        print("That is not a valid option please try again")
    else:
        if help_eli == 'y':
            begin_game()
            break
        else:
            clear()
            print("Eli won't be getting any help this time")
            print("\nThanks for playing")
            break
