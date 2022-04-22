# Repeatedly ask the user to enter game scores in a format like team1 score1 - team2 score2. 
# Store this information in a dictionary where the keys are the team names and the values are lists of the form [wins, losses].

def GameScore():
    team_dict = {}
    while True:
        team = input("Enter team name: ")
        if team == "":
            break
        score = input("Enter score: ")
        team_dict[team] = score
    while True:
        team = input("Enter team name: ")
        if team == "":
            break
        if team in team_dict:
            print(team_dict[team])
        else:
            print("Team not in dictionary")
    print("\n")
    for key in sorted(team_dict.keys()):
        print(key, team_dict[key])

GameScore()