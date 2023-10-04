

class Team:

    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

def create_teams():
    global teams 
    team1 = Team('attackers', 80, 20)
    team2 = Team('deffenders', 30, 70)
    team3 = Team('Averages', 50, 50)
    teams = [team1, team2, team3]

def play():
    print('Debug: play()')

play()