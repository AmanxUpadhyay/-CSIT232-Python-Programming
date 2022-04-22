# Repeatedly ask the user to enter a team name and the how many games the team won and how many they lost. 
# Store this information in a dictionary where the keys are the team names and the values are lists of the form [wins, losses].
# (a) Using the dictionary created above, allow the user to enter a team name and print out the team’s winning percentage.
# (b) Using the dictionary, create a list whose entries are the number of wins of each team.
# (c) Using the dictionary, create a list of all those teams that have winning records.

def Game_Record():
    team_dict = {}
    while True:
        team = input("Enter team name: ")
        if team == "":
            break
        wins = input("Enter number of wins: ")
        losses = input("Enter number of losses: ")
        team_dict[team] = [wins, losses]
    while True:
        team = input("Enter team name: ")
        if team == "":
            break
        if team in team_dict:
            print(team_dict[team][0], "/", team_dict[team][1], "=", float(team_dict[team][0]) / float(team_dict[team][1]))
        else:
            print("Team not in dictionary")
    print("\n")
    for key in sorted(team_dict.keys()):
        print(key, team_dict[key][0], "/", team_dict[key][1], "=", float(team_dict[key][0]) / float(team_dict[key][1]))

Game_Record()