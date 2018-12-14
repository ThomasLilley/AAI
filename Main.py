import sys
import csv
import random
import numpy as np


sample_size = 1000000  # global variable


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

    # dictionary of variables and their corresponding parents, also the column no in the csv file
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
        'C': [10, 'AL', 'LC'],
        'LC': [11, 'S', 'G']
    }

    # a dictionary to store the calculated probabilities
    p_values = {
        'S': [0, 0, 0, 0],
        'YF': [],
        'AN': [],
        'PP': [],
        'G': [],
        'AD': [0, 0],
        'BED': [],
        'CA': [0, 0, 0, 0],
        'F': [0, 0, 0, 0],
        'AL': [],
        'C': [0, 0, 0, 0],
        'LC': [0, 0, 0, 0]
    }
    # order is: 0,0,0,0, :  TT, TF, FT, FF

    for p_var, value in variables.items():
        if len(value) == 1:  # infer no parents

            (ttl_true, ttl_false) = (no_parents(value[0]))

            p_values[p_var] = (ttl_true + 1) / (ttl_true+ttl_false+2)
            # print(p_var, 'NO PARENTS total true:', ttl_true, 'total false:', ttl_false,
            # 'Probability:', p_values[p_var])
            # print(p_var, ':', p_values[p_var])

        if len(value) == 2:  # infer one parent

            parent = variables[value[1]]
            parent = parent[0]
            (ttl_true, ttl_false, ttl_y) = one_parent(value[0], parent)

            p_values[p_var] = (ttl_true + 1) / (ttl_y + 2)

            # print(p_var, ':', p_values[p_var])

        if len(value) == 3:  # infer two parents
            parent1 = variables[value[1]]
            parent1 = parent1[0]

            parent2 = variables[value[2]]
            parent2 = parent2[0]

            (x_y_z, y_z, x_not_y_z, not_y_z, x_y_not_z, y_not_z, x_not_y_not_z, not_y_not_z) \
                = two_parent(value[0], parent1, parent2)

            # print(x_y_z, y_z, x_not_y_z, not_y_z, x_y_not_z, y_not_z, x_not_y_not_z, not_y_not_z)

            p_values[p_var][0] = (x_y_z + 1) / (y_z + 2)
            p_values[p_var][1] = (x_not_y_z + 1) / (not_y_z + 2)
            p_values[p_var][2] = (x_y_not_z + 1) / (y_not_z + 2)
            p_values[p_var][3] = (x_not_y_not_z + 1) / (not_y_not_z + 2)

            # print(p_var, ':', p_values[p_var])

    # generate a random, sample data set for prior sampling
    print("Begin Prior Sampling (sample size 1 Million)...")
    samples = sample_gen()
    prior = prior_sampling(samples, p_values)
    answer = reject_sampling(prior)
    print("\nProbability of P(S|C=True, F=True): ", answer)


def prior_sampling(sample, values):
    cols = 9
    sample_data_set = np.zeros((sample_size, cols))

    for i in range(cols):
        for j in range(sample_size):
            if i == 0:  # ANXIETY
                if sample[j][i] < values['AN']:
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 1:  # PEER PRESSURE
                if sample[j][i] < values['PP']:
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 2:  # SMOKING
                if sample[j][i] < (values['S'][0]) and sample_data_set[j][1] == 1 and sample_data_set[j][0] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['S'][1]) and sample_data_set[j][1] == 0 and sample_data_set[j][0] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['S'][2]) and sample_data_set[j][1] == 1 and sample_data_set[j][0] == 0:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['S'][3]) and sample_data_set[j][1] == 0 and sample_data_set[j][0] == 0:
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 3:  # GENETICS
                if sample[j][i] < (values['G']):
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 4:  # BED
                if sample[j][i] < (values['BED']):
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 5:  # LUNG CANCER
                if sample[j][i] < (values['LC'][0]) and sample_data_set[j][3] == 1 and sample_data_set[j][2] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['LC'][1]) and sample_data_set[j][3] == 0 and sample_data_set[j][2] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['LC'][2]) and sample_data_set[j][3] == 1 and sample_data_set[j][2] == 0:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['LC'][3]) and sample_data_set[j][3] == 0 and sample_data_set[j][2] == 0:
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 6:  # ALLERGY
                if sample[j][i] < (values['AL']):
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 7:  # COUGHING
                if sample[j][i] < (values['C'][0]) and sample_data_set[j][5] == 1 and sample_data_set[j][6] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['C'][1]) and sample_data_set[j][6] == 0 and sample_data_set[j][5] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['C'][2]) and sample_data_set[j][6] == 1 and sample_data_set[j][5] == 0:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['C'][3]) and sample_data_set[j][5] == 0 and sample_data_set[j][6] == 0:
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0
            elif i == 8:  # FATIGUE
                if sample[j][i] < (values['F'][0]) and sample_data_set[j][5] == 1 and sample_data_set[j][7] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['F'][1]) and sample_data_set[j][7] == 0 and sample_data_set[j][5] == 1:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['F'][2]) and sample_data_set[j][7] == 1 and sample_data_set[j][5] == 0:
                    sample_data_set[j][i] = 1
                elif sample[j][i] < (values['F'][3]) and sample_data_set[j][5] == 0 and sample_data_set[j][7] == 0:
                    sample_data_set[j][i] = 1
                else:
                    sample_data_set[j][i] = 0

    # print(sample_data_set)

    return sample_data_set


def reject_sampling(prior):
    # cols = 9
    p_of_s_given_c_f = 0
    p_of_not_s_given_c_f = 0
    untrue = 0

    for i in range(sample_size):
        if prior[i][2] == 1 and prior[i][7] == 1 and prior[i][8] == 1:
            p_of_s_given_c_f += 1
        if prior[i][2] == 0 and prior[i][7] == 1 and prior[i][8] == 1:
            p_of_not_s_given_c_f += 1
        else:
            untrue += 1

    # print("p(S|C=True, F=True) :", p_of_s_given_c_f, "p(¬S|C=True, F=True) :", p_of_not_s_given_c_f,
    #     "false values", untrue)

    normalised = p_of_s_given_c_f * (1/(p_of_s_given_c_f+p_of_not_s_given_c_f))

    return normalised


def sample_gen():
    cols = 9
    sample_data_set = np.zeros((sample_size, cols))
    # print(sample_data_set)

    for i in range(sample_size):
        for j in range(cols):
            sample_data_set[i][j] = float(random.randint(0, 10000)/10000)

    # print(sample_data_set)
    return sample_data_set


def no_parents(col):

    # takes 1 arg, column of csv file and calculates no of true/ false values
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


def one_parent(col_x, col_y):  # takes two column no's as arguments
    total_true = 0
    total_false = 0
    total_y = 0

    file = open('lucas0_train.csv', 'r')
    reader = csv.reader(file)

    for row in reader:
        if row[col_x] == '1' and row[col_y] == '1':
            total_true += 1
        if row[col_x] == '0' or row[col_y] == '0':
            total_false += 1
        if row[col_y] == '1':
            total_y += 1
    file.close()

    return total_true, total_false, total_y


def two_parent(col_x, col_y, col_z):

    x_y_z = 0
    y_z = 0

    x_not_y_z = 0
    not_y_z = 0

    x_y_not_z = 0
    y_not_z = 0

    x_not_y_not_z = 0
    not_y_not_z = 0

    file = open('lucas0_train.csv', 'r')
    reader = csv.reader(file)

    for row in reader:
        # xyz true
        if row[col_x] == '1' and row[col_y] == '1' and row[col_z] == '1':
            x_y_z += 1
        if row[col_y] == '1' and row[col_z] == '1':
            y_z += 1

        # x not y z
        if row[col_x] == '1' and row[col_y] == '0' and row[col_z] == '1':
            x_not_y_z += 1
        if row[col_y] == '0' and row[col_z] == '1':
            not_y_z += 1

        # x y not z
        if row[col_x] == '1' and row[col_y] == '1' and row[col_z] == '0':
            x_y_not_z += 1
        if row[col_y] == '1' and row[col_z] == '0':
            y_not_z += 1

        # x not y not z
        if row[col_x] == '1' and row[col_y] == '0' and row[col_z] == '0':
            x_not_y_not_z += 1
        if row[col_y] == '0' and row[col_z] == '0':
            not_y_not_z += 1

    file.close()

    return x_y_z, y_z, x_not_y_z, not_y_z, x_y_not_z, y_not_z, x_not_y_not_z, not_y_not_z


def task2():
    print('task2')


menu = False
print(" _______________________________________")
print("| AAI ASSIGNMENT 1 | THOMAS LILLEY 2018 |")
print("|_______________________________________|")
while not menu:

    # Main level menu
    print(' _______________________________________')
    print('| Main Menu                             |')
    print('|_______________________________________|')
    print('| 1) TASKS ON PROBABILITIES             |')
    print('| 2) TASK ON HIDDEN MARKOV MODELS       |')
    print('| 3) Exit                               |')
    print('|_______________________________________|')
    opt1 = input('Please Select An Option: ')

    # menu for tasks on probability menu level 2
    if opt1 == '1':

        print('\n _______________________________________')
        print('| TASKS ON PROBABILITIES                |')
        print('|_______________________________________|')
        print('| 1) TASK 1.A                           |')
        print('| 2) TASK 1.B                           |')
        print('| 3) Back to Main Menu                  |')
        print('|_______________________________________|')
        opt2 = input('Please Select An Option: ')
        if opt2 == '1':
            print('\nTask 1.A')
            print('Please provide the following probabilities:')
            s = task1a()
            print('The Probability of having the disease given the test is positive, is:')
            print('p(d|t):', s)
        elif opt2 == '2':
            task1b()
        elif opt2 == '3':
            # loops round to main menu
            print('\n')
        else:
            print('Invalid Input, Try Again: \n')

    # menu for tasks on markov models level 2
    elif opt1 == '2':
        print('\n _______________________________________')
        print('| TASK ON HIDDEN MARKOV MODELS          |')
        print('|_______________________________________|')
        print('| 1) Task on hidden markov models       |')
        print('| 2) Back to Main Menu                  |')
        print('|_______________________________________|')
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


print('out of menu loop, this should not happen!')



