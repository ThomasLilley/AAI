import sys

menu = False

while not menu:
    # Main level menu
    print("\n|---------------------------------------")
    print("| Main Menu")
    print("|---------------------------------------")
    print("| 1) TASKS ON PROBABILITIES")
    print("| 2) TASK ON HIDDEN MARKOV MODELS ")
    print("| 3) Exit")
    print("|---------------------------------------")
    opt1 = input("Please Select An Option: ")

    # menu for tasks on probability menu level 2
    if opt1 == '1':

        print("\n|---------------------------------------")
        print('| TASKS ON PROBABILITIES ')
        print("|---------------------------------------")
        print('| 1)')
        print('| 2)')
        print('| 3) Back to Main Menu')
        print("|---------------------------------------")
        opt2 = input("Please Select An Option: ")
        if opt2 == '1':
            print("Function call here")
        elif opt2 == '2':
            print("B")
        elif opt2 == '3':
            print("C")
        else:
            print("Invalid Input, Try Again: \n")

    # menu for tasks on markov models level 2
    elif opt1 == '2':
        menu = True
        print("\n|---------------------------------------")
        print('| TASK ON HIDDEN MARKOV MODELS')
        print("|---------------------------------------")
        print('| 1)')
        print('| 2)')
        print('| 3) Back to Main Menu')
        print("|---------------------------------------")
        opt2 = input("Please Select An Option: ")
        if opt2 == '1':
            print()
        elif opt2 == '2':
            print()
        elif opt2 == '3':
            print()
        else:
            print("Invalid Input, Try Again: \n")
    elif opt1 == '3':
        sys.exit(0)
    else:
        print('Invalid Input, Try again: \n')


print("out of menu loop")
