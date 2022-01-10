


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
    first_Choice = input("What choice do you want to make? ( 1 / 2 ): ")
    if first_Choice == '1':
        print()
        choice1()
    elif first_Choice == '2':
        print()
        choice2()


    



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
help_Eli = input("Would you like to help Eli escape from the police? (Y / N): ")
if help_Eli == 'n' or help_Eli == 'N':
    print("Eli won't be getting any help this time")
elif help_Eli == 'y' or help_Eli == 'Y':
    begin_Game()