import random
import numpy as np
hands = np.array(['rock', 'scissors', 'paper'])

    # Prints the message to start the game
def start_message():
    print("Start 'rock-paper-scissors' game")

        # Print the index of each hand along with the hand's name.
def get_player():
    i = 0
    for hand in enumerate(hands):
        print(f'{i}:{hand}')
        i += 1
    hand = input('Select a hand')
    return hand

    # Generates a random number between 0 and 2 as the computer's hand
def get_computer():
    comp = random.randint(0, 2)
    return comp

    # Returns the name of the hand based on the given index
def get_hand_name(choice):
    return hands[int(choice)]

    # Prints the player's and computer's hands
def view_hand(player, computer):
    print('My hand is', get_hand_name(player))
    print('Computer\'s hand is', get_hand_name(computer))

    # Prints the result of the game based on the given parameter
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