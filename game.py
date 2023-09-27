import random

def start_message():
    print("Start ‘rock-paper-scissors’ game")

def get_player():
    hand = input('0=rock, 1=scissors, 2=paper \n')
    return hand

def get_computer():
    comp = random.randint(0, 2)
    return comp

def get_hand_name(choice):
    hands = ['rock', 'scissors', 'paper']
    return hands[int(choice)]

def view_hand(player, computer):
    print('My hand is', get_hand_name(player))
    print('Computer\'s hand is', get_hand_name(computer))

def view_result(res):
    results={'win':'you win', 'lose':'you lose', 'draw':'draw try again'}
    print(results[res])

def is_hand(any):
    if any.isdigit():
        no = int(any)
        if no >= 0 and no <= 2:
            return True
        else:
            return False
    else:
        return False


def get_result(hands, comp):
    hand = int(hands)
    if hand == comp:
        return 'draw'
    elif (hand == 0 and comp == 1) or (hand == 1 and comp == 2) or (hand == 2 and comp == 0):
        return 'win'
    else:
        return 'lose'

def initializer(): 
    hand = get_player()
    while is_hand(hand) == False:
        print('Please enter number between 0 and 2')
        hand = get_player()

    comp = get_computer()

    view_hand(hand, comp)

    print(get_result(hand, comp))

    if get_result(hand, comp) == 'draw':
        initializer()

start_message()
initializer()