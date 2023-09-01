import random

# print("Start ‘rock-paper-scissors’ game")
# print("Input your hand choice")

# hand = int(input('0=rock, 1=scissors, 2=paper2 \n'))
# comp = random.randint(0, 2)

# print('Your hand is', hand)
# print('Computers hand is', comp)

# if hand == comp:
#     print('Draw')
# elif (hand == 0 and comp == 1) or (hand == 1 and comp == 2) or (hand == 2 and comp == 0):
#     print('win')
# else:
#     print('Loose')

hands = ['rock', 'scissors', 'paper2']

def start_message():
    print("Start ‘rock-paper-scissors’ game")

def get_player():
    hand = int(input('0=rock, 1=scissors, 2=paper2 \n'))
    print('your hand is', hands[hand])
    return hand

def get_computer():
    comp = random.randint(0, 2)
    print('comp hand is', hands[comp])
    return comp

def view_result(get_player, get_computer):
    if get_player == get_computer:
        print('Draw try again')
        print("\n --------------------------\n\n")
        initializer()
    elif (get_player == 0 and get_computer == 1) or (get_player == 1 and get_computer == 2) or (get_player == 2 and get_computer == 0):
        print('you win')
        print("\n --------------------------\n\n")
    else:
        print('you Loose')
        print("\n --------------------------\n\n")

def initializer():
    start_message()
    hand = get_player()
    comp = get_computer()
    view_result(hand, comp)

initializer()