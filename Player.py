class Player:
	#main player keeps track of score, nights played, etc etc
	nights_played = -1
	score = 0.0
	skill = 0
	name = "n/a"

	def __init__(self, n):
		self.name = n

	def getScore(self):
		return self.score

	def getNightsPlayed(self):
		return self.nights_played

	def getSkill(self):
		return self.skill