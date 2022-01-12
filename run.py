


def begin_Game():
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

def choice1():
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

def choice1_1():
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

def choice1_1a():
    print()
    print("As Eli rides through the brown dirt path, the motorbike starts to slow down.")
    print("So he stops by a diner in the middle of no where only to discover that he is low on fuel.")
    print("He leaves the bike at the diner and continues on foot through the thick forest behind the diner.")
    print("The police finds his motorbike but cannot find him")
    print("Eli is able escape with all the bags of cash intact.")
    print("Eli is now a very rich man living freely.")
    print()
    print("CONGRATULATIONS. YOU WIN !!!!!")
    print()
    print("Click on the RUN PROGRAM button to restart the game")

def choice1_1b():
    print()
    print("As he rides through the black dirt path, Eli gets to a tunnel.")
    print("Unknown to him there are policemen waiting on the other side of the tunnel.")
    print("As he gets closer to the other side, the police catch him by slamming into his motorbike with their cop car")
    print("Eli falls to the ground with all his bags of cash and the police arrest him.")
    print("")
    print("That is the end of the road for Eli.")
    print()
    print()
    begin_Game()





def choice1_2():
    print()

def choice1_3():
    print()

def choice2():
    print()


    



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
help_Eli = input("Would you like to help Eli escape from the police? (Y / N):\n ")
if help_Eli == 'n' or help_Eli == 'N':
    print("Eli won't be getting any help this time")
elif help_Eli == 'y' or help_Eli == 'Y':
    begin_Game()