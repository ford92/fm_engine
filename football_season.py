import random
import operator
import teams
from player import Player, Keeper
from stats import Statistics, SeasonStatistics
import plotly.graph_objects as go
from plotly import offline

"""
def kick_off():
	print(f"{team[0].title()} kick off and {team[i].name} has the ball.")
"""


"""player_decision will prompt player in possession to either dribble, pass or shoot
(shoot only an option if sufficient number of passes/dribbles have been completed)"""
def player_decision():
	global position
	global passes
	global dribbles

	# check_position if == True will allow player to shoot
	check_position()

	
	if position == True:
		#print(f"{team[i].name} is in a good position, will he take a shot?\n")
		team_stats[i -1].update_shots()

		# Update season stats
		for player in season_players:
			if player.name == team[i].name:
				player.shots += 1

		if v_team[1].shooting_battle(team[i]) == True:
			team_stats[i -1].update_goals()
			# Update season stats
			for player in season_players:
				if player.name == team[i].name:
					player.goals += 1
			update_score()
			position = False
			change_team()
			#kick_off()
		else:
			change_team()

	"""Depending on the player's strongest attribute, this will determine whether player will pass or dribble
	This will then initiate a 'battle' of attributes to determine whether successful outcome of the pass/dribble"""
	if team[i].passing >= team[i].dribbling:
		a = random.randint(0, 1 + team[i].passing - team[i].dribbling)
		if a == 0:
			if team[i].dribble_battle(v_team[random.randint(2, len(team) - 1)]) == True:
				dribbles += 1
				team_stats[i - 1].update_dribbles_complete()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.dribbles_complete += 1

				player_decision()
			else: 
				team_stats[i-1].update_dribbles_tackled()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.dribbles_tackled += 1
				change_team()


		else:
			if team[i].passing_battle() == True:
				passes += 1
				team_stats[i - 1].update_passes_complete()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.passes_complete += 1
				change_player()
				player_decision()
			else:
				team_stats[i - 1].update_passes_missed()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.passes_missed += 1
				change_team()

	else:
		a = random.randint(0, 1 + team[i].dribbling - team[i].passing)
		if a == 0:
			if team[i].passing_battle() == True:
				passes += 1
				team_stats[i - 1].update_passes_complete()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.passes_complete += 1
				change_player()
				player_decision()
			else:
				team_stats[i - 1].update_passes_missed()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.passes_missed += 1
				change_team()
	

		else:
			if team[i].dribble_battle(v_team[random.randint(2, len(team) - 1)]) == True:
				dribbles += 1
				team_stats[i - 1].update_dribbles_complete()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.dribbles_complete += 1
				player_decision()
			else:
				team_stats[i - 1].update_dribbles_tackled()
				# Update season stats
				for player in season_players:
					if player.name == team[i].name:
						player.dribbles_tackled += 1
				change_team()

"""Checks if team are in a position to shoot. This will
 be after at least 3 passes have been completed or 4 dribbles."""
def check_position():
	global position
	global passes
	global dribbles

	if passes >= 3 or dribbles >= 4:
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
	#print(f"{minute}' min")

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

	#print(f"The score is {team_a[0]} - {team_a_goals}, {team_b[0]} - {team_b_goals}\n")

# Prints final score and updates team's statistics
def final_score():
	#print("\nThat's the final whistle. The score is:\n")
	print(f"{team_a[0]}: {team_a_goals} - {team_a_scorers} \n{team_b[0]}: {team_b_goals} - {team_b_scorers}\n")
	if team_a_goals > team_b_goals:
		for team in season_teams:
			if team.team == team_a[0]:
				team.wins += 1
				team.points += 3
				team.goal_difference += (team_a_goals) - (team_b_goals)
			elif team.team == team_b[0]:
				team.losses += 1
				team.goal_difference += (team_b_goals) - (team_a_goals)
	elif team_b_goals > team_a_goals:
		for team in season_teams:
			if team.team == team_b[0]:
				team.wins += 1
				team.points += 3
				team.goal_difference += (team_b_goals) - (team_a_goals)
			elif team.team == team_a[0]:
				team.losses += 1
				team.goal_difference += (team_a_goals) - (team_b_goals)

	else:
		for team in season_teams:
			if team.team == team_a[0]:
				team.draws += 1
			elif team.team == team_b[0]:
				team.draws += 1



""" List all teams with SeasonStatistics instance allow updates from completed matches.
Takes arguments 'team name', points, wins, draws, losses, goal_difference"""

season_teams = []
for team in teams.total_teams:
	season_teams.append(SeasonStatistics(team[0], 0, 0, 0, 0, 0, ''))

season_players = []
for team in teams.total_teams:
	i = 1
	while i < 12:
		season_players.append(Statistics(team[i].name, 0, 0, 0, 0, 0, 0))
		i +=1


# Initiate Match Engine
# Each team will iterate through every other team and match will be simulated.
# Team A is the 'home' team
# Team B is the 'away' team
for team_a in teams.total_teams:
	for team_b in teams.total_teams:
		
		team = team_a
		team_a_stats = []
		team_stats = team_a_stats
		j = 1
		while j < 12:

			person = Statistics(team_a[j].name, 0, 0, 0, 0, 0, 0)
			team_a_stats.append(person)
			j+=1

		team_a_goals = 0
		team_a_scorers = []

		if team_b == team_a:
			continue
		else:
			v_team = team_b
			print(f"{team_a[0]} vs {team_b[0]}")


		
		# Initialise opponent team's stats
		team_b_stats = []
		k = 1
		while k < 12:

			person = Statistics(team_b[k].name, 0, 0, 0, 0, 0, 0)
			team_b_stats.append(person)
			k+=1

		team_b_goals = 0
		team_b_scorers = []

		# Random player will be selected to have possession of the ball
		i = random.randint(2, 11)

		# Initialise stats to zero before each game starts
		minute = 0
		passes = 0
		dribbles = 0
		position = False

		# Initiate match engine
		#kick_off()
		while minute < 90:
			player_decision()
			
		final_score()


# Once season program has been completed. Record all data in tables.
# Arrange and output a final table standings

season_teams.sort(key=operator.attrgetter('goal_difference'), reverse=True)
season_teams.sort(key=operator.attrgetter('points'), reverse=True)

teams = []
points = []
wins = []
draws = []
losses = []
goal_difference = []

for team in season_teams:
	teams.append(team.team)
	points.append(team.points)
	wins.append(team.wins)
	draws.append(team.draws)
	losses.append(team.losses)
	goal_difference.append(team.goal_difference)

fig_1 = go.Figure(data=[go.Table(header = dict(values=['Position', 'Team', 'Points', 'Wins', 'Draws', 'Losses', 'Goal Difference']), 
	cells = dict(values=[list(range(1,21)), teams, points, wins, draws, losses, goal_difference]))])

offline.plot(fig_1, filename='league_table.html')

# Arrange and output top scorers table

season_players.sort(key=operator.attrgetter('goals'), reverse=True)
season_players = season_players[:10]

scorer_name = []
player_goals = []

for player in season_players:
	scorer_name.append(player.name)
	player_goals.append(player.goals)

fig_2 = go.Figure(data=[go.Table(header = dict(values=['Player', 'Goals']), 
	cells = dict(values=[scorer_name, player_goals]))])

offline.plot(fig_2, filename='scorers.html')


# Arrange and output players with most shots table

season_players.sort(key=operator.attrgetter('shots'), reverse=True)
season_players = season_players[:10]

shots_name = []
player_shots = []

for player in season_players:
	shots_name.append(player.name)
	player_shots.append(player.shots)

fig_2 = go.Figure(data=[go.Table(header = dict(values=['Player', 'Shots']), 
	cells = dict(values=[shots_name, player_shots]))])

offline.plot(fig_2, filename='most_shots.html')


# Arrange and output players with most passes complete table

season_players.sort(key=operator.attrgetter('passes_complete'), reverse=True)
season_players = season_players[:10]

passes_name = []
player_passes = []

for player in season_players:
	passes_name.append(player.name)
	player_passes.append(player.passes_complete)

fig_3 = go.Figure(data=[go.Table(header = dict(values=['Player', 'Successful Passes']), 
	cells = dict(values=[passes_name, player_passes]))])

offline.plot(fig_3, filename='most_passes.html')


# Arrange and output players with most dribbles complete table

season_players.sort(key=operator.attrgetter('dribbles_complete'), reverse=True)
season_players = season_players[:10]

dribbles_name = []
player_dribbles = []

for player in season_players:
	dribbles_name.append(player.name)
	player_dribbles.append(player.dribbles_complete)

fig_4 = go.Figure(data=[go.Table(header = dict(values=['Player', 'Successful Dribbles']), 
	cells = dict(values=[dribbles_name, player_dribbles]))])

offline.plot(fig_4, filename='most_dribbles.html')







