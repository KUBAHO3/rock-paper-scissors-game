# importing necessary libraries
import random
import math

# Defining assets for the game
data = [['O','0'], ['l','1'], ['u','v']]
col_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

level = 1
col = 5
row = 4

def start_message():
    print('Start')

# Showing game level
def section_message():
    print('A'+ str(level))

# function to change input string to a number of unique character
def change_input_number(input_str):
    str_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    input_str_split = list(input_str)
    col_represantation = input_str_split[0]
    row_represantation = int(input_str_split[1])
    col_number = str_dictionary[col_represantation]
    row_number = row_represantation - 1
    input_number = row_number * col + col_number
    return input_number


def view_question():
    choice_data = random.randint(0,2) # choosing array to display in game randomly
    different_number = random.randint(0, (col * row) - 1 ) # selecting unique number to display
    print('different number '+ str(different_number + 1))  # printing index of unique number
    qn = data[choice_data]
    print(qn) # printing the selected array for the game

    # pre initial auxiliaries
    aux_init = '/|'
    aux_separator = '--'

    # generating & printing column auxiliaries dynamically
    k = 0
    while k < col:
        aux_init += col_data[k]
        aux_separator += '-'
        k += 1
    print(aux_init)
    print(aux_separator)

    # printing rows of data
    i = 0
    j = 0
    while i < row:
        string = str(i + 1) + '|'
        while j < col:
            if (i * col + j) == different_number: # appending unique character in the output
                string += qn[1]
            else:
                string += qn[0]
            j += 1
        print(string)
        i += 1
        j = 0
    return different_number # returning unique string index

# Checking if the user input converted index equal to unique string index
def is_correct_number(different_number, input_number):
    if input_number == different_number:
        return True
    else:
        return False
    
# Function to change unique string index to its position string
def change_string(number):
    col_number = number % col
    row_number = math.floor(number / col) + 1
    correct_string = col_data[col_number] + str(row_number)
    return correct_string
    
# Function to print the results of the game pass or fail with correction.
def view_result(is_correct, diff_num):
    if is_correct:
        print('Correct')
    else:
        print('Wrong')
        print('Diff no: ', diff_num + 1)
        print('Correct answer: ', change_string(diff_num))

# Main function or center of operations
def play():
    section_message()
    diff_num = view_question()
    in_string = input('Input the deifferent carracter e.g: A3 \n')
    print('Your choice is: ', in_string)
    input_number = change_input_number(in_string)
    print('Your input no is: ', input_number)
    is_correct = is_correct_number(diff_num, input_number)
    view_result(is_correct, diff_num)

start_message()  # calling function to print the start message
play() # calling the main function