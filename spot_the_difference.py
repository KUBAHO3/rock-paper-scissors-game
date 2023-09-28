import random
data = [['O','0'], ['l','1'], ['u','v']]

def start_message():
    print('Start')

def section_message():
    level = 1
    print('A'+ str(level))

def view_question():
    choice = random.randint(0,2)
    qn = data[choice]
    print(qn)
    i = 0
    j = 0
    string = ''
    while i < 3:
        while j < 3:
            string += qn[0]
            j += 1
        print(string)
        i += 1

def play():
    section_message()
    view_question()

start_message()
play()