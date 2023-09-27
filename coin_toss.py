import random

def start_message():
    print("Start ‘coin toss’ game")

def get_user_bet():
    bet = input('Input your bet \n')
    return bet


def is_correct_input(input_string):
    if input_string.isdigit():
        input_number = int(input_string)
        if input_number == 0 or input_number == 1:
            return True
        else:
            return False
    else:
        return False
    
def get_coin_side():
    coin = random.randint(0,1)
    return coin

def get_side_name(side):
    sides = ['head', 'tail']
    return sides[int(side)]

def view_side(bet, side):
    print('My bet is', bet)
    print('Coin is', side)

def get_result(bet, side):
    if bet == side:
        return 'win'
    else:
        return 'lose'
    
def view_result(results):
    print(results)

def play():
    bet = get_user_bet()
    while is_correct_input(bet) == False:
        print('please bet between 0 an 1')
        bet = get_user_bet()


    side = get_coin_side()

    bet_name = get_side_name(bet)
    side_name = get_side_name(side)

    view_side(bet_name, side_name)

    print(get_result(bet_name, side_name))

start_message()
play()