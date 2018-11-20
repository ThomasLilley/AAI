import sys


def task1a():
    p_of_d = 0.0
    p_of_not_t_given_not_d = 0.0
    p_of_t_given_d = 0.0
    # input handling with exception catching
    flag = False
    while not flag:
        try:
            p_of_d = float(input("P(d) : "))
            p_of_t_given_d = float(input("P(t|d) : "))
            p_of_not_t_given_not_d = float(input("P(¬t|¬d) : "))
            flag = True
        except ValueError:
            print("invalid input, try again")
            flag = False

    # calculate missing probabilities
    p_of_not_d = 1 - p_of_d
    p_of_t_given_not_d = 1 - p_of_not_t_given_not_d

    p_of_t = (p_of_t_given_d * p_of_d) + (p_of_t_given_not_d*p_of_not_d)

    # Bayes Theorem
    p_of_d_given_t = (p_of_t_given_d*p_of_d)/p_of_t
    # return p(d|t)
    return p_of_d_given_t


def task1b():
    print("task1b")


def task2():
    print("task2")


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
        print('| 1) TASK 1.A')
        print('| 2) TASK 1.B')
        print('| 3) Back to Main Menu')
        print("|---------------------------------------")
        opt2 = input("Please Select An Option: ")
        if opt2 == '1':
            print("\nTask 1.A")
            print("Please provide the following probabilities:")
            s = task1a()
            print("The Probability of having the disease given the test is positive, is:")
            print("p(d|t):", s)
        elif opt2 == '2':
            print("Task 1.B")
            task1b()
            print("-")
        elif opt2 == '3':
            # loops round to main menu
            print("\n")
        else:
            print("Invalid Input, Try Again: \n")

    # menu for tasks on markov models level 2
    elif opt1 == '2':
        print("\n|---------------------------------------")
        print('| TASK ON HIDDEN MARKOV MODELS')
        print("|---------------------------------------")
        print('| 1)')
        print('| 2) Back to Main Menu')
        print("|---------------------------------------")
        opt2 = input("Please Select An Option: ")
        if opt2 == '1':
            print()
        elif opt2 == '2':
            # loops round to main menu
            print("\n")
        else:
            print("Invalid Input, Try Again: \n")
    elif opt1 == '3':
        # ends the program gracefully
        sys.exit(0)
    else:
        print('Invalid Input, Try again: \n')


print("out of menu loop")



