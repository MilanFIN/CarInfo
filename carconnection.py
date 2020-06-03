class CarConnection():
	def __init__(self):
		pass
		self.throttle = 0
		self.throttleaddition = 1

	def getValue(self, label):
		if (label == "rpm"):
			return "1000"
		elif (label == "gear"):
			return "1"
		elif (label == "speed"):
			return "45"
		elif (label == "fuelpercentage"):
			return "30"
		elif (label == "throttle"): #percentages
			self.throttle += self.throttleaddition
			if (self.throttle >= 100 or self.throttle <= 0):
				self.throttleaddition *= -1
			return str(self.throttle)
		return "test"