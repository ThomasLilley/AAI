import sys

menu1 = False
menu2 = False

while not menu1:
    print("----------------------------------------")
    print("| Main Menu\n| \n| 1) TASKS ON PROBABILITIES \n| 2) TASK ON HIDDEN MARKOV MODELS ")
    print("| 3) Exit\n|")
    print("----------------------------------------")
    opt1 = input("Please Select An Option: ")

    if opt1 == '1':
        print('opt 1')
        menu1 = True
    elif opt1 == '2':
        print('opt 2')
        menu1 = True
    elif opt1 == '3':
        sys.exit(0)
    else:
        print('\n Invalid Input, Try again: \n')


print("out of menu loop")
