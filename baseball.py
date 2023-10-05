import random
import math

teams = []
playing_teams = {'myself': False, 'enemy': False}

class Team:

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.total_score=0

    def info(self):
        print(self.name + ': offensive power: '+ str(self.attack) + ' / defensive power: '+ str(self.defense))

    def get_hit_rate(self):
        offense = random.randint(10, self.attack)
        return offense
    
    def get_out_rate(self):
        defense = random.randint(10, self.defense)
        return defense
    

def create_teams():
    global teams 
    team1 = Team('attackers', 80, 20)
    team2 = Team('deffenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]

def show_teams():
    print('Information of all teams')
    for team in teams:
        print(teams.index(team) + 1)
        team.info()

def choice_team(player):
    player_name = ''
    if player == 'myself':
        player_name = 'your'
    elif player == 'enemy':
        player_name = 'opponent\'s'

    choice_team_number = int(input('Select '+player_name+' team by input(1-3): '))
    playing_teams[player] = teams[choice_team_number - 1]
    print(player_name + 'team is '+ playing_teams[player].name)

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

def play():
    print('Debug: play()')
    create_teams()
    show_teams()
    choice_team('myself')
    choice_team('enemy')

    score_boards = ['________|', 'You     |','Opponent|']
    for i in range(1,10):
        score_boards[0] += str(i) + '|'
        inning_score = get_play_inning('top')
        score_boards[1] += str(inning_score) + '|'
        playing_teams['myself'].total_score += inning_score

        if i == 9 and playing_teams['enemy'].total_score > playing_teams['myself'].total_score:
            score_boards[2] += 'X|'
        else:
            inning_score = get_play_inning('bottom')
            score_boards[2] += str(inning_score) + '|'
            playing_teams['enemy'].total_score += inning_score
    score_boards[0] += 'R｜'
    score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'
    for score in score_boards:
        print(score)
play()