import random
import math

data = [['O','0'], ['l','1'], ['u','v']]
col_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

level = 1
col = 5
row = 4

def start_message():
    print('Start')

def section_message():
    print('A'+ str(level))

def change_input_number(input_str):
    str_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
    input_str_split = list(input_str)
    col_represantation = input_str_split[0]
    row_represantation = int(input_str_split[1])
    col_number = str_dictionary[col_represantation]
    row_number = row_represantation - 1
    input_number = row_number * row + col_number
    return input_number


def view_question():
    choice = random.randint(0,2)
    different_number = random.randint(0, (col * row) - 1 )
    print('different number '+ str(different_number + 1))
    qn = data[choice]
    print(qn)
    print('/|ABCDE\n-------')
    i = 0
    j = 0
    while i < row:
        string = str(i + 1) + '|'
        while j < col:
            if (i * col + j) == different_number:
                string += qn[1]
            else:
                string += qn[0]
            j += 1
        print(string)
        i += 1
        j = 0
    return different_number

def is_correct_number(different_number, input_number):
    if input_number == different_number:
        return True
    else:
        return False
    
def change_string(number):
    col_number = number % col
    row_number = math.floor(number / row) + 1
    correct_string = col_data[col_number] + str(row_number)
    return correct_string
    
def view_result(is_correct, diff_num):
    if is_correct:
        print('Correct')
    else:
        print('Wrong')
        print('Diff no: ', diff_num + 1)
        print('Correct answer: ', change_string(diff_num))


def play():
    section_message()
    diff_num = view_question()
    in_string = input('Input the deifferent carracter e.g: A3 \n')
    print('Your choice is: ', in_string)
    input_number = change_input_number(in_string)
    print('Your input no is: ', input_number)
    is_correct = is_correct_number(diff_num, input_number)
    view_result(is_correct, diff_num)
    # print(change_string(11))

start_message()
play()