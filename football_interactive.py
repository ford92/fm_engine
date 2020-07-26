import random
import teams
from player import Player, Keeper
from stats import Statistics


def coin_toss(club_a, club_b):
	global team
	global team_stats
	global v_team

	coin = random.randint(1, 2)
	if coin == 1:
		team = team_a
		team_stats = team_a_stats
		v_team = team_b
	elif coin == 2:
		team = team_b
		team_stats = team_b_stats
		v_team = team_a

def kick_off():
	print(f"{team[0].title()} kick off and {team[i].name} has the ball.")

"""player_decision will prompt player in possession to either dribble, pass or shoot
(shoot only an option if sufficient number of passes/dribbles have been completed)"""
def player_decision():
	global position
	global passes
	global dribbles

	# check_position if == True will allow player to shoot
	check_position()

	
	if position == True:
		print(f"{team[i].name} is in a good position, will he take a shot?\n")
		team_stats[i -1].update_shots()
		if v_team[1].shooting_battle(team[i]) == True:
			team_stats[i -1].update_goals()
			update_score()
			position = False
			change_team()
			kick_off()
		else:
			change_team()

	"""Depending on the player's strongest attribute, this will determine whether player will pass or dribble
	This will then initiate a 'battle' of attributes to determine whether successful outcome of the pass/dribble"""
	if team[i].passing >= team[i].dribbling:
		a = random.randint(0, 1 + team[i].passing - team[i].dribbling)
		if a == 0:
			if team[i].dribble_battle(v_team[random.randint(2, len(team) - 1)]) == True:
				dribbles += 1
				team_stats[i -1].update_dribbles_complete()
				player_decision()
			else: 
				team_stats[i-1].update_dribbles_tackled()
				change_team()


		else:
			if team[i].passing_battle() == True:
				passes += 1
				team_stats[i - 1].update_passes_complete()
				change_player()
				player_decision()
			else:
				team_stats[i - 1].update_passes_missed()
				change_team()

	else:
		a = random.randint(0, 1 + team[i].dribbling - team[i].passing)
		if a == 0:
			if team[i].passing_battle() == True:
				passes += 1
				team_stats[i - 1].update_passes_complete()
				change_player()
				player_decision()
			else:
				team_stats[i - 1].update_passes_missed()
				change_team()
	

		else:
			if team[i].dribble_battle(v_team[random.randint(2, len(team) - 1)]) == True:
				dribbles += 1
				team_stats[i -1].update_dribbles_complete()
				player_decision()
			else:
				team_stats[i-1].update_dribbles_tackled()
				change_team()

"""Checks if team are in a position to shoot. This will
 be after at least 3 passes have been completed or 4 dribbles."""
def check_position():
	global position
	global passes
	global dribbles

	if passes >= 5 or dribbles >= 4:
		position = True
		passes = 0
		dribbles = 0
	
	else:
		position = False

# Selects a random player from the team to have possession
def change_player():
	global i
	while True:
		a = random.randint(2, len(team)-1)
		if a != i: break

	i = a

# Changes team in possession and relative stats
def change_team():
	global team
	global team_stats
	global v_team
	global minute
	global passes
	global dribbles

	if team == team_a:
		team = team_b
		team_stats = team_b_stats
		v_team = team_a
	else:
		team = team_a
		team_stats = team_a_stats
		v_team = team_b

	passes = 0
	dribbles = 0
	update_minute()

# Updates the match minute
def update_minute():
	global minute

	a = random.randint(1,5)
	minute += a
	print(f"{minute}' min")

# Updates scoreline and records goal scorers
def update_score():
	global team_a_goals
	global team_b_goals
	global team_a_scorers
	global team_b_scorers

	if team == team_a:
		team_a_goals += 1
		team_a_scorers.append(team[i].name)

	else:
		team_b_goals += 1
		team_b_scorers.append(team[i].name)

	print(f"The score is {team_a[0]} - {team_a_goals}, {team_b[0]} - {team_b_goals}\n")


# Prompts user to select two teams to play
teams.select_team()

# Populates the chosen home team with the team from teams.py
team_a = [teams.team_1[0], teams.team_1[1], teams.team_1[2], teams.team_1[3], 
teams.team_1[4], teams.team_1[5], teams.team_1[6], teams.team_1[7], 
teams.team_1[8], teams.team_1[9], teams.team_1[10], teams.team_1[11]]


#Initiate statistics for each player
team_a_stats = []
j = 1
while j < 12:

	person = Statistics(team_a[j].name, 0, 0, 0, 0, 0, 0)
	team_a_stats.append(person)
	j+=1

team_a_goals = 0
team_a_scorers = []

# Populates the chosen away team with the team from teams.py
team_b = [teams.team_2[0], teams.team_2[1], teams.team_2[2], teams.team_2[3], 
teams.team_2[4], teams.team_2[5], teams.team_2[6], teams.team_2[7], 
teams.team_2[8], teams.team_2[9], teams.team_2[10], teams.team_2[11]]

#Initiate statistics for each player
team_b_stats = []
k = 1
while k < 12:

	person = Statistics(team_b[k].name, 0, 0, 0, 0, 0, 0)
	team_b_stats.append(person)
	k+=1

team_b_goals = 0
team_b_scorers = []



# Zero-value minutes, passes, dribbles and position flag to False   

minute = 0
passes = 0
dribbles = 0
position = False


# Coin toss will randomly select team to kick off
coin_toss(teams.team_1[0], teams.team_2[0])
i = random.randint(2, 11)
kick_off()
minute = 0

# Being loop with player making decisions until the 90+ minute
while minute < 90:
	player_decision()
	

print("\nThat's the final whistle. The score is:\n")
print(f"{team_a[0]}: {team_a_goals} - {team_a_scorers} \n{team_b[0]}: {team_b_goals} - {team_b_scorers}\n")



"""Outputs both teams match statistics for each outfield player"""

m = 1

while m < 11:
	team_a_stats[m].print_statistics()
	m += 1

print("\n")

n = 1

while n < 11:
	team_b_stats[n].print_statistics()
	n += 1










