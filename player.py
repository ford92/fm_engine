import random

class Keeper:
	# Class for Keepers that takes 2 arguments. The Keeper's name and their goalkeeping 'ability'
	def __init__(self, name, ability):
		self.name = name
		self.ability = ability

	# Initiates a battle of ability between the Keeper's ability attribute and the opposing player's shooting attribute	
	def shooting_battle(self, opponent):
		self.opponent = opponent
		if self.opponent.shooting >= self.ability:
			a = random.randint(0, (1 + self.opponent.shooting - self.ability))
			if a == 0:
				#print(f"\n{self.name} has saved {self.opponent.name}'s shot!\n")
				return False
			else:
				#print(f"\n{self.opponent.name} SHOOTS AND SCORES!\n")
				return True	

		else:
			a = random.randint(0, (1 + self.ability - self.opponent.shooting))
			if a == 0:
				#print(f"\n{self.opponent.name} SHOOTS AND SCORES!\n")
				return True
			else:
				#print(f"\n{self.name} has saved {self.opponent.name}'s shot!\n")
				return False


class Player:
	""" Class for outfield Players. Takes 5 arguments, player's name and their attributes for passing
		shooting, dribbling and tackling"""
	def __init__(self, name, passing, shooting, dribbling, tackling):
		self.name = name
		self.passing = passing
		self.shooting = shooting
		self.dribbling = dribbling
		self.tackling = tackling

	""" Initiates a battle of attributes between the player's dribbling attribute and a randomly chosen
	opposing player's tackling ability"""
	def dribble_battle(self, opponent):

		self.opponent = opponent

		if self.dribbling >= self.opponent.tackling:
			a = random.randint(0, (1 + self.dribbling - self.opponent.tackling))
			if a == 0 or a == 1:
				#print(f"{self.opponent.name} has dispossessed {self.name}")
				return False
			else:
				#print(f"{self.name} performed a successful dribble past {self.opponent.name}")
				return True

		else:
			a = random.randint(0,(1 + self.opponent.tackling - self.dribbling))
			if a == 0:
				#print(f"{self.name} performed a successful dribble past {self.opponent.name}")
				return True
			else:
				#print(f"{self.opponent.name} has dispossessed {self.name}")
				return False

	"""Calculates the chance of a successful pass"""
	def passing_battle(self):

		b = random.randint(0, (self.passing))
		if b == 0:
			#print(f"{self.name} has misplaced his pass")
			return False
		else:
			#print(f"{self.name} has successfully completed a pass.")
			return True















			

