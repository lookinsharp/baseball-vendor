class Weather:
	#weather during the night of the game
	temperature = -1
	parcipitation = "none"
	#forcast is an array of strings; each index corresponds to one hour of the day 
	#so forcast[0] = hour 12 midnight, forcast[1] = hour 1 am, etc etc
	forecast = []
	month = "n/a";

	def __init__(self, temp, p, month, f):
		self.temperature = temp
		self.parcipitation = p
		self.forecast = f
		self.month = month

	def getTemp(self):
		return self.temperature

	def getParcipitation(self):
		return self.parcipitation

	def getForecast(self):
		return self.forecast

	def setTemp(self, temp):
		#to do, make something that sets the temperature
		self.temperature = temp
	
	def updateTemp(self, time):
		#updates the temperature
		#temperature will be in farenheight (for now bc thats what I use) based on month
		#if time is greater than 8pm, decrease temp 
		if(time >= 20):
			self.temp -= .5
		#for now, as long as there is some time of parcipitation, decrease the temperature
		if(parcipitation != none):
			self.temp -= .5



	def setParcipitation(self, p):
		#to do, set parcipation -- maybe take in date?
		self.parcipation = p

	def updateParcipitation(self, time):
		#set the parcipation to be the one stored in the array at the correct time
		self.parcipation = self.forcast[time]

	def setForecast(self, f):
		#generate and set a forcast -- actually maybe combine this with getforecast
		self.forcast = f

	#updates a section of forcast starting at given hour, ending when forcast list runs out
	def updateForcastSome(self, hour_start, new_forcast):
		if new_forcast.length > 24:
			raise Exception("Forcast longer than 24 hours not allowed")
		int cur = hour_start
		for i in range (0, new_forcast.length):
			if cur >= self.forcast.length:
				cur = 0
			self.forcast[cur] = new_forcast[i]


































