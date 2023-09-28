import random
data = [['O','0'], ['l','1'], ['u','v']]

def start_message():
    print('Start')

def section_message():
    level = 1
    print('A'+ str(level))

def view_question():
    choice = random.randint(0,2)
    print(data[choice])

def play():
    section_message()
    view_question()

start_message()
play()