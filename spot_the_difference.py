import random
data = [['O','0'], ['l','1'], ['u','v']]

def start_message():
    print('Start')

def section_message():
    level = 1
    print('A'+ str(level))

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

start_message()
play()