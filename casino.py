import random

# initialize empty lists
players = []
table = []
cells = []

# define a Player class to represent a player
class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin
    self.bets = {}
    self.reset_table()

  def set_bet_coin(self, bet_coin, bet_cell):
    # subtract the bet coin from the player's coin
    self.coin -= bet_coin
    # add the bet cell and bet coin to the player's bets dictionary
    self.bets[bet_cell] = bet_coin
    # print a message to show that the player has placed a bet
    print(self.name + ' placed ' + str(bet_coin) + ' coins on ' + bet_cell + '.')

  def reset_table(self):
    # reset all bets to zero for each cell on the table
    for cell in table:
      self.bets.update({cell.name: 0})

# define a Human class that inherits from the Player class
class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    # determine the maximum bet coin based on the player's remaining coin
    if self.coin >= 99:
      max_bet_coin = 99
    else:
      max_bet_coin = self.coin
    # prompt the player to enter a bet coin amount
    bet_message = 'How many coins do you want to bet? (1-' + str(max_bet_coin) + ')'
    bet_coin = input(bet_message)
    # validate the bet coin input and prompt again if it's invalid
    while not self.enable_bet_coin(bet_coin, max_bet_coin):
      bet_coin = input(bet_message)
    # prompt the player to enter a bet cell
    bet_message = 'Where do you want to bet? (R,B,1-8)'
    bet_cell = input(bet_message)
    # validate the bet cell input and prompt again if it's invalid
    while not self.enable_bet_cell(bet_cell):
      bet_cell = input(bet_message)
    # call the set_bet_coin method to place the bet
    super().set_bet_coin(int(bet_coin), bet_cell)

  def enable_bet_coin(self, string, max_bet_coin):
    # check if the input is a valid integer within the range of 1 to max_bet_coin
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= max_bet_coin:
        return True
      else:
        return False
    else:
      return False

  def enable_bet_cell(self, string):
    # check if the input is a valid cell number or color (R or B)
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= 8:
        return True
      else:
        return False
    else:
      if string == 'R' or string == 'B':
        return True
      else:
        return False

# define a Computer class that inherits from the Player class
class Computer(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    # determine the maximum bet coin based on the player's remaining coin
    if self.coin >= 99:
      max_bet_coin = 99
    else:
      max_bet_coin = self.coin
    # choose a random bet coin amount between 1 and max_bet_coin
    bet_coin = random.randint(1, max_bet_coin)
    # choose a random cell to place the bet on
    bet_cell_number = random.randint(0, len(cells) - 1)
    bet_cell = cells[bet_cell_number]
    # call the set_bet_coin method to place the bet
    super().set_bet_coin(bet_coin, bet_cell)

# define a Cell class to represent a cell on the table
class Cell:
  def __init__(self, name, rate, color):
    self.name = name
    self.rate = rate
    self.color = color

# define a ColorBase class to store ANSI escape codes for coloring text in the console
class ColorBase:
  BLACK = '\033[30m'
  RED = '\033[31m'
  GREEN = '\033[32m'
  END = '\033[0m'

# define a function to populate the cells list with cell names from the table list
def set_cells():
  global cells
  cells = []
  for cell in table:
    cells.append(cell.__dict__['name'])

# define a function to create player objects and add them to the players list
def create_players():
  global players
  players.append(Human('MY', 500))
  players.append(Computer('C1', 500))
  players.append(Computer('C2', 500))
  players.append(Computer('C3', 500))

# define a function to loop through all players and prompt them to place bets
def bet_players():
  for player in players:
    player.bet()

# define a function to randomly select a hit cell and check if any players have won
def check_hit():
  hit_cell_number = random.randint(0, len(cells) - 1)
  hit_cell = cells[hit_cell_number]
  print('The hit cell is "' + hit_cell + '".')
  for player in players:
    if player.bets[hit_cell] >= 1:
      win_player(player, hit_cell_number)

# define a function to calculate and award winnings to a winning player
def win_player(player, hit_cell_number):
  hit_cell = cells[hit_cell_number]
  win_coin = player.bets[hit_cell] * table[hit_cell_number].rate
  player.coin += win_coin
  print(player.name + ' won ' + str(win_coin) + ' coins!')

# define a function to display each player's remaining coin balance
def show_coin():
  message = '[Coin Balance] '
  for player in players:
    message += player.name + ':' + str(player.coin) + ' / '
  print(message)

# define a function to create the table by adding Cell objects to the table list
def create_table():
  global table
  table.append(Cell('R', 8, 'red'))
  table.append(Cell('B', 8, 'black'))
  table.append(Cell('1', 2, 'red'))
  table.append(Cell('2', 2, 'black'))
  table.append(Cell('3', 2, 'red'))
  table.append(Cell('4', 2, 'black'))
  table.append(Cell('5', 2, 'red'))
  table.append(Cell('6', 2, 'black'))
  table.append(Cell('7', 2, 'red'))
  table.append(Cell('8', 2, 'black'))

# define a function to display the current state of the table and each player's bets on it
def show_table():
  row = green_bar() + '_____' + green_bar()
  for player in players:
    row += player.name + green_bar()
  print(row)
 
  for cell in table:
    row = green_bar() + color(cell.color, cell.name + '(x' + str(cell.rate) + ')') + green_bar()
    for player in players:
      row += str(player.bets[cell.name]).zfill(2) + green_bar()
    print(row)

# define a function to reset all bets on the table for each player before starting a new round of betting
def reset_table():
  for player in players:
    player.reset_table()

# define a function to color text in the console based on its color name (red or green)
def color(color_name, string):
  if color_name == 'red':
    return ColorBase.RED + string + ColorBase.END
  elif color_name == 'green':
    return ColorBase.GREEN + string + ColorBase.END
  else:
    return string

# define a function to return a green-colored vertical bar character for use in displaying the table
def green_bar():
  return color('green', '|')

# define an initialization function that creates the table, players, and cells lists
def initialize():
  create_table()
  create_players()
  set_cells()

# define a function that runs through one round of betting and checking for hits on the table
def play_once():
  reset_table()
  bet_players()
  show_table()
  check_hit()
  show_coin()

# define a function that checks if any players have run out of coins and ends the game if so
def is_game_end():
  for player in players:
    if player.coin <= 0:
      return True
  return False

# define a function that prints a message indicating which player has run out of coins and ends the game
def game_end():
  for player in players:
    if player.coin <= 0:
      print(player.name + " has run out of coins. Game over.")

# define a function that initializes the game and loops through rounds of play until it ends 
def play():
  initialize()
  show_coin()
  while not is_game_end():
    play_once()
  else:
    game_end()

play()
