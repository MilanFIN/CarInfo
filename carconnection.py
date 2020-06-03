


class CarConnection():
	def __init__(self):
		pass

	def getValue(self, label):
		if (label == "rpm"):
			return "1000"
		elif (label == "gear"):
			return "1"
		elif (label == "speed"):
			return "45"
		elif (label == "fuelpercentage"):
			return "30"
		return "test"