import sys
import csv


def task1a():
    p_of_d = 0.0
    p_of_not_t_given_not_d = 0.0
    p_of_t_given_d = 0.0
    # input handling with exception catching
    flag = False
    while not flag:
        try:
            p_of_d = float(input('P(d) : '))
            p_of_t_given_d = float(input('P(t|d) : '))
            p_of_not_t_given_not_d = float(input('P(¬t|¬d) : '))
            flag = True
        except ValueError:
            print('invalid input, try again')
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

    variables = {
        'S': [0, 'AN', 'PP'],
        'YF': [1, 'S'],
        'AN': [2],
        'PP': [3],
        'G': [4],
        'AD': [5, 'G'],
        'BED': [6],
        'CA': [7, 'AD', 'F'],
        'F': [8, 'LC', 'C'],
        'AL': [9],
        'C': [10],
        'LC': [11, 'S', 'G']
    }

    p_values = {
        'S': []*4,
        'YF': [],
        'AN': [],
        'PP': [],
        'G': [],
        'AD': []*2,
        'BED': [],
        'CA': []*4,
        'F': []*4,
        'AL': [],
        'C': []*4,
        'LC': []*4
    }

    for p_var, value in variables.items():
        if len(value) == 1:  # infer no parents

            (ttl_true, ttl_false) = (no_parents(value[0]))

            p_values[p_var] = (ttl_true + 1) / (ttl_true+ttl_false+2)
            print(p_var, 'NO PARENTS total true:', ttl_true, 'total false:', ttl_false, 'Probability:', p_values[p_var])

        if len(value) == 2:  # infer one parent

            parent = variables[value[1]]
            parent = parent[0]
            (ttl_true, ttl_false, ttl_y) = one_parent(value[0], parent)

            p_values[p_var] = (ttl_true + 1) / (ttl_y + 2)

            print(p_var, 'ONE PARENT  total true:', ttl_true, 'total false:', ttl_false, 'probability:', p_values[p_var])

        if len(value) == 3:  # infer two parents
            parent1 = variables[value[1]]
            parent1 = parent1[0]

            parent2 = variables[value[2]]
            parent2 = parent2[0]
            (ttl_true, ttl_y_z, y_true_z_false, y_false_z_true) = two_parent(value[0], parent1, parent2)
            p_values[p_var[0]] = (ttl_true + 1)/(ttl_y_z + 2)  # both parents true

            p_values[p_var[1]] = 0  # *********TEMP********** #

            print(p_var, 'TWO PARENTS  total true:', ttl_true, 'total y_z:', ttl_y_z,
                  'probability:', p_values[p_var])


def no_parents(col):

    total_true = 0
    total_false = 0

    file = open('lucas0_train.csv', 'r')
    reader = csv.reader(file)

    for row in reader:
        if row[col] == '1':
            total_true += 1
        if row[col] == '0':
            total_false += 1
    file.close()

    return total_true, total_false


def one_parent(col1, col2):
    total_true = 0
    total_false = 0
    total_y = 0

    file = open('lucas0_train.csv', 'r')
    reader = csv.reader(file)

    for row in reader:
        if row[col1] == '1' and row[col2] == '1':
            total_true += 1
        if row[col1] == '0' or row[col2] == '0':
            total_false += 1
        if row[col2] == '1':
            total_y += 1
    file.close()

    return total_true, total_false, total_y


def two_parent(col_x, col_y, col_z):
    total_true = 0
    total_false = 0
    y_z_true = 0
    y_z_false = 0

    y_true_z_false = 0
    y_false_z_true = 0


    file = open('lucas0_train.csv', 'r')
    reader = csv.reader(file)

    for row in reader:
        # y true z true
        if row[col_y] == '1' and row[col_z] == '1':
            y_z_true += 1
        if row[col_x] == '1' and row[col_y] == '1' and row[col_z] == '1':
            total_true += 1

        # y false z false
        if row[col_x] == '0' and row[col_y] == '0' and row[col_z] == '0':
            total_false += 1
        if row[col_y] == '0' and row[col_z] == '0':
            y_z_false += 1

        # y false z true
        if row[col_y] == '0' and row[col_z] == '1':
            y_false_z_true += 1

        # y true z false
        if row[col_y] == '1' and row[col_z] == '0':
            y_true_z_false += 1

    file.close()
    return total_true, y_z_true, y_true_z_false, y_false_z_true,


def task2():
    print('task2')


menu = False

while not menu:
    # Main level menu
    print('\n|---------------------------------------')
    print('| Main Menu')
    print('|---------------------------------------')
    print('| 1) TASKS ON PROBABILITIES')
    print('| 2) TASK ON HIDDEN MARKOV MODELS ')
    print('| 3) Exit')
    print('|---------------------------------------')
    opt1 = input('Please Select An Option: ')

    # menu for tasks on probability menu level 2
    if opt1 == '1':

        print('\n|---------------------------------------')
        print('| TASKS ON PROBABILITIES ')
        print('|---------------------------------------')
        print('| 1) TASK 1.A')
        print('| 2) TASK 1.B')
        print('| 3) Back to Main Menu')
        print('|---------------------------------------')
        opt2 = input('Please Select An Option: ')
        if opt2 == '1':
            print('\nTask 1.A')
            print('Please provide the following probabilities:')
            s = task1a()
            print('The Probability of having the disease given the test is positive, is:')
            print('p(d|t):', s)
        elif opt2 == '2':
            print('Task 1.B')
            task1b()
        elif opt2 == '3':
            # loops round to main menu
            print('\n')
        else:
            print('Invalid Input, Try Again: \n')

    # menu for tasks on markov models level 2
    elif opt1 == '2':
        print('\n|---------------------------------------')
        print('| TASK ON HIDDEN MARKOV MODELS')
        print('|---------------------------------------')
        print('| 1)')
        print('| 2) Back to Main Menu')
        print('|---------------------------------------')
        opt2 = input('Please Select An Option: ')
        if opt2 == '1':
            print()
        elif opt2 == '2':
            # loops round to main menu
            print('\n')
        else:
            print('Invalid Input, Try Again: \n')
    elif opt1 == '3':
        # ends the program gracefully
        sys.exit(0)
    else:
        print('Invalid Input, Try again: \n')


print('out of menu loop')



