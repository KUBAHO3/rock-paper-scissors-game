
teams = []
playing_teams = {'myself': False, 'enemy': False}

class Team:

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def info(self):
        print(self.name + ': offensive power: '+ str(self.attack) + ' / defensive power: '+ str(self.defense))

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

def play():
    print('Debug: play()')
    create_teams()
    show_teams()
    choice_team('myseld')
    choice_team('enemy')

play()