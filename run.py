import os
from os import system, name


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def begin_game():
    clear()
    print()
    print("Eli just robbed the Central Bank of the world.")
    print("Eli is trying to escape with large bags of cash.")
    print("The police have been alerted and are in hot pursuit.")
    print("Help Eli escape from the police.")
    print()
    print("Eli storms out of the bank on to the busy road.")
    print("He comes up to a fork at the end of the road.")
    print("He is faced with two choices: ")
    print()
    print("Choice 1:  Turn left.")
    print("Choice 2:  Turn right.")
    print()
    first_choice = input("What choice do you want to make? ( 1 / 2 ):\n ")
    if first_choice == '1':
        print()
        choice1()
    elif first_choice == '2':
        print()
        choice2()
    else:
        if first_choice not in [1, 2]:
            print("That is not a valid option, please try again")


def choice1():
    clear()
    print()
    print("He turns left to a narrow path that leads him up to a shed.")
    print("He breaks open the doors to the shed.")
    print("He looks around for anything that can help him escape.")
    print("He finds an open safe that contains three keys: ")
    print()
    print("Choice 1:  keys to a motorbike.")
    print("Choice 2:  keys to a car.")
    print("Choice 3:  keys to a boat.")
    print()
    second_choice = input("Pick a key ( 1 / 2 / 3 ):\n ")
    if second_choice == '1':
        print()
        choice1_1()
    elif second_choice == '2':
        print()
        choice1_2()
    elif second_choice == '3':
        print()
        choice1_3()
    else:
        if second_choice not in [1, 2, 3]:
            print("That is not a valid option, please try again")


def choice1_1():
    clear()
    print()
    print("Eli takes the keys to the motorbike.")
    print("He starts the motorbike.")
    print("He keeps riding till he comes up to the main road.")
    print("The main road leads to 3 coloured dirt paths:")
    print()
    print("choice 1:  The brown dirt path")
    print("choice 2:  The black dirt path")
    print("choice 3:  The grey dirt path")
    print()
    third_choice = input("Choose a dirt path ( 1 / 2 / 3 ):\n ")
    if third_choice == '1':
        print()
        choice1_1a()
    elif third_choice == '2':
        print()
        choice1_1b()
    elif third_choice == '3':
        print()
        choice1_1c()
    else:
        if third_choice not in [1, 2, 3]:
            print("That is not a valid option, please try again")


def choice1_1a():
    clear()
    print()
    print(
        "As Eli rides through the brown dirt path, "
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
    print()
    print("CONGRATULATIONS. YOU WIN !!!!!")
    print()
    print("Click on the RUN PROGRAM button to restart the game")


def choice1_1b():
    clear()
    print()
    print("As he rides through the black dirt path, Eli gets to a tunnel.")
    print(
        "Unknown to him there are policemen waiting " 
        "on the other side of the tunnel.")
    print(
        "As he gets closer to the other side, the police catch him " 
        "by slamming into his motorbike with their cop car")
    print(
        "Eli falls to the ground with all his bags of cash " 
        "and the police arrest him.")
    print()
    print("That is the end of the road for Eli.")
    print()
    print()
    begin_game()


def choice1_1c():
    clear()
    print()
    print(
        "As he rides through the grey dirt path, " 
        "his bike starts to slow down.")
    print("He discovers that he is low on fuel.")
    print(
        "With no place to stop and refuel, "
        "the bike finally comes to a stop on the road.")
    print("He is now on open land with no cover to hide under.")
    print("The police finally spot him.")
    print("He is arrested and all the stolen cash is recovered.")
    print()
    print()
    begin_game()


def choice1_2():
    clear()
    print()
    print(
        "Eli takes the keys to the car,"
        "enters the car and starts driving.")
    print(
        "Not long after he starts driving he hears the police sirens "
        "getting closer and the chase begins. ")
    print(
        "As he drives up the main road, "
        " he comes to a path leading to 2 bridges: ")
    print()
    print("choice 1:  Bridge 1")
    print("choice 2:  Bridge 2")
    print()
    fourth_choice = input("Choose which bridge to take ( 1 / 2 ):\n ")
    if fourth_choice == '1':
        print()
        choice1_2a()
    elif fourth_choice == '2':
        print()
        choice1_2b()
    else:
        if fourth_choice not in [1, 2]:
            print("That is not a valid option, please try again")


def choice1_2a():
    clear()
    print()
    print(
        "As Eli drives through bridge 1, "
        "the car starts to skid and then overturns.")
    print(
        "He climbs out of the car and starts to run across the bridge, "
        "but the bridge is broken half way.")
    print("The police surrounds him and he is arrested.")
    print()
    print()
    begin_game()


def choice1_2b():
    clear()
    print()
    print(
        "As Eli drives on to bridge 2, "
        "he sees something at the end of the bridge.")
    print(
        "The end of the bridge has been blocked off "
        "by a broken down fuel tanker.")
    print("He jumps out of the car and makes a run for it.")
    print("He is not fast enough and so the Police catch him.")
    print()
    print()
    begin_game()


def choice1_3():
    clear()
    print()
    print(
        "Eli takes the keys to the boat and runs "
        "to the nearby river where he finds the boat parked "
        "and also a scuba gear with an oxygen tank. ")
    print("All he has to do is to choose either: ")
    print("choice 1:  The boat")
    print("choice 2:  The scuba gear")
    print()
    fifth_choice = input("Which would you like to choose ( 1 / 2 ):\n ")
    if fifth_choice == '1':
        print()
        choice1_3a()
    elif fifth_choice == '2':
        print()
        choice1_3b()
    else:
        if fifth_choice not in [1, 2]:
            print("That is not a valid option, please try again")


def choice1_3a():
    clear()
    print()
    print("Eli takes the scuba gear.")
    print("Decides to swim out into the river.")
    print("Unknown to him, there is not enough oxygen in the oxygen tank.")
    print("He drowns after swimming for a few minutes.")
    print()
    print()


def choice1_3b():
    clear()
    print()
    print(
        "Eli decides to use the boat but as he moves along the river, "
        "he discovers that there is a  huge hole in the boat. ")
    print("The boat starts to sink very quickly.")
    print(
        "As he does not know how to swim, "
        "he ends up in the river and drowns.")


def choice2():
    clear()
    print()
    print("Eli turns right to a wide path that leads up to a house.")
    print("He could either:")
    print("choice 1: Try to break in from the front")
    print("choice 2: Try to break in from the back")
    print("choice 3: Use the hidden key under the door mat")
    print()
    sixth_choice = input("Which choice do you want? ( 1 / 2 / 3 ):\n ")
    if sixth_choice == '1':
        print()
        print(
            "He tries to break in from the front, "
            "but the door is rock solid.")
        print("The police catch up to him and he is arrested.")
    elif sixth_choice == '2':
        print()
        print(
            "He tries to break in from the back "
            "by using a large rock to break the window.")
        print(
            "He climbs into the house to hide, "
            "but the owner of the house raises an alarm "
            "which gets the attention of the police near by.")
        print("Eli surrenders.")
    elif sixth_choice == '3':
        print()
        print("He uses the hidden key under the mat.")
        print("He opens the door and makes his way into the living room to hide.")
        print("A massive guard dog sees him.")
        print("The dog starts barking and attacks him.")
        print(
            "Eli screams and tries to fight off the dog, "
            "but the owner of the house calls the police and he is arrested")
    else:
        if sixth_choice not in [1, 2, 3]:
            print("That is not a valid option, please try again")


clear()
print()
print()
print("    #####################")
print("    #                   #")
print("    #  Help Eli Escape  #")
print("    #                   #")
print("    #####################")
print()
print()
print("Eli just robbed the Central Bank of the world.")
print("Eli is trying to escape with large bags of cash.")
print()
while True:
    help_eli = input("Would you like to help Eli escape from the police? (Y / N):\n ").lower().strip()
    if help_eli not in ["y", "n"]:
        print("That is not a valid option please try again")
    else:
        if help_eli == 'y':
            begin_game()
            break
        else:
            print("Eli won't be getting any help this time")
            break
