class Weather:
	#weather during the night of the game
	temperature = -1
	parcipitation = "none"
	forecast = "none"

	def __init__(self, temp, p):
		self.temperature = temp
		self.parcipitation = p
		self.forecast = "none"

	def getTemp(self):
		return self.temperature

	def getParcipitation(self):
		return self.parcipitation

	def getForecast(self):
		return self.forecast

	def setTemp(self):
		#to do, make something that sets the temperature

	def setParcipitation(self):
		#to do, set parcipation -- maybe take in date?

	def setForecast(self):
		#generate and set a forcast -- actually maybe combine this with getforecast