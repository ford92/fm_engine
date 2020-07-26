class Statistics:
	"""Track players statistics throughout the season"""
	def __init__ (self, name, goals, shots, passes_complete, passes_missed, dribbles_complete, dribbles_tackled):

		self.name = name
		self.goals = goals
		self.shots = shots
		self.passes_complete = passes_complete
		self.passes_missed = passes_missed
		self.dribbles_complete = dribbles_complete
		self.dribbles_tackled = dribbles_tackled


	def update_goals(self):
		self.goals += 1

	def update_shots(self):
		self.shots += 1

	def update_passes_complete(self):
		self.passes_complete += 1

	def update_passes_missed(self):
		self.passes_missed += 1

	def update_dribbles_complete(self):
		self.dribbles_complete += 1

	def update_dribbles_tackled(self):
		self.dribbles_tackled += 1

	def pass_success(self):
		self.pass_completion =  100*(self.passes_complete)/(self.passes_complete + self.passes_missed)

	def print_statistics(self):
		if (self.passes_complete + self.passes_missed) == 0:
			self.pass_completion = 0
		else:
			self.pass_completion =  int(100*(self.passes_complete)/(self.passes_complete + self.passes_missed))

		if (self.dribbles_complete + self.dribbles_tackled) == 0:
			self.dribbles_completion = 0
		else:
			self.dribbles_completion = int(100*(self.dribbles_complete)/(self.dribbles_complete + self.dribbles_tackled))

		print(f"{self.name}, {self.goals} goals, {self.shots} shots, {self.passes_complete} passes completed, {self.pass_completion}% pass completion," 
			f" {self.dribbles_complete} dribbles completed, {self.dribbles_completion}% dribble success")



class SeasonStatistics:

	def __init__ (self, team, points, wins, draws, losses, 
		goal_difference, top_scorer):

		self.team = team
		self.points = points 
		self.wins = wins
		self.draws = draws
		self.losses = losses
		self.goal_difference = goal_difference
		self.top_scorer = top_scorer

