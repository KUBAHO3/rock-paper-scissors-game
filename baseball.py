# Import necessary dependencies
import random
import math

# Define core assets
teams = []
playing_teams = {'myself': False, 'enemy': False}

# Team class and methods
class Team:
    # Constructor function which contain all the instances attributes
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.total_score=0
    # Instance display function by accessing constructor and prints its attributes
    def info(self):
        print(self.name + ': offensive power: '+ str(self.attack) + ' / defensive power: '+ str(self.defense))
    # Choosing attack score randomly and returning the offense
    def get_hit_rate(self):
        offense = random.randint(10, self.attack)
        return offense
    # Choosing defense score randomly and returning the defense
    def get_out_rate(self):
        defense = random.randint(10, self.defense)
        return defense
    
# Instance creator and assign them into global variable teams
def create_teams():
    global teams 
    team1 = Team('attackers', 80, 20)
    team2 = Team('deffenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]
# All instamce displayer by looping through teams array
def show_teams():
    print('Information of all teams')
    for team in teams:
        print(teams.index(team) + 1)
        team.info()
# Team type selector with unique player name which depend on passed string
def choice_team(player):
    player_name = ''
    if player == 'myself':
        player_name = 'your'
    elif player == 'enemy':
        player_name = 'opponent\'s'

    choice_team_number = int(input('Select '+ player_name +' team by input(1-3): '))
    playing_teams[player] = teams[choice_team_number - 1]
    print(player_name + ' team is '+ playing_teams[player].name)
# Inning score assigner from Team classes methodc wether top or bottom and return the score
def  get_play_inning(inner):
    if inner == 'top':
        hit_rate = playing_teams['myself'].get_hit_rate()
        out_rate = playing_teams['enemy'].get_out_rate()
    elif inner == 'bottom':
        hit_rate = playing_teams['enemy'].get_hit_rate()
        out_rate = playing_teams['myself'].get_out_rate()
    inning_score = math.floor((hit_rate - out_rate) / 10)

    if inning_score < 0:
        inning_score = 0
    return inning_score
# Main function of the program to connect methods and Team class
def play():
    print('Welcome to baseball game!!!!')
    create_teams()
    show_teams()
    choice_team('myself')
    choice_team('enemy')
    # Generating scores of nine games by using for loop
    score_boards = ['________|', 'You     |','Opponent|']
    for i in range(1,10):
        score_boards[0] += str(i) + '|'
        inning_score = get_play_inning('top')
        score_boards[1] += str(inning_score) + '|'
        playing_teams['myself'].total_score += inning_score
        # Ignoring last score of opponent if they are ahead in scores
        if i == 9 and playing_teams['enemy'].total_score > playing_teams['myself'].total_score:
            score_boards[2] += 'X|'
        else:
            inning_score = get_play_inning('bottom')
            score_boards[2] += str(inning_score) + '|'
            playing_teams['enemy'].total_score += inning_score
    # Printing the total scores for each team
    score_boards[0] += 'R｜'
    score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'
    # Scoreboard output loop in scoreboards array
    for score in score_boards:
        print(score)

play() # program initializer