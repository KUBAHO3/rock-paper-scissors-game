import random
data = [['O','0'], ['l','1'], ['u','v']]

def start_message():
    print('Start')

def section_message():
    level = 1
    print('A'+ str(level))

def change_input_number(input_str):
    str_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    input_str_split = list(input_str)
    col_represantation = input_str_split[0]
    row_represantation = int(input_str_split[1])
    col_number = str_dictionary[col_represantation]
    row_number = row_represantation - 1
    input_number = row_number * 3 + col_number
    return input_number


def view_question():
    choice = random.randint(0,2)
    different_number = random.randint(0,8)
    print('different number '+ str(different_number + 1))
    qn = data[choice]
    print(qn)
    print('/|ABC\n-----')
    i = 0
    j = 0
    while i < 3:
        string = str(i + 1) + '|'
        while j < 3:
            if (i * 3 + j) == different_number:
                string += qn[1]
            else:
                string += qn[0]
            j += 1
        print(string)
        i += 1
        j = 0

def play():
    section_message()
    view_question()
    in_string = input('Input the deifferent carracter e.g: A3 \n')
    print(change_input_number(in_string))

start_message()
play()