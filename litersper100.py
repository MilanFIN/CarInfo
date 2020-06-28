import time

FUELTANKSIZE = 60 #liters, opel vectra c = 60
#csv: fuel in liters, distance in km
FILEPATH = "./storage/litersper100.txt"
SAVEFREQUENCY = 300 # interval of saving in seconds

class LitersPer100():
	def __init__(self):
		
		self.fuelUsed = 0.0
		self.drivenDistance = 0.0

		with open(FILEPATH) as f:
			content = f.readlines()

		content = [x.strip() for x in content] 
		if (len(content) != 0):
			values = [x.strip() for x in content[0].split(',')]
			if (len(values) == 2):
				self.fuelUsed = float(values[0])
				self.drivenDistance = float(values[1])

		self.lastSaveTime = time.time()

		self.lastSpeed = 0.0
		self.lastFuel = 0.0


		self.speedUpdateTime = time.time()

	def reset(self):
		line = "0, 0"
		with open(FILEPATH, 'w') as f:
			f.write(line)
		self.lastSaveTime = time.time()
		self.__init__()


	def save(self):
		if (time.time() - self.lastSaveTime >= SAVEFREQUENCY):
			line = str(self.fuelUsed) + ", " + str(self.drivenDistance)
			with open(FILEPATH, 'w') as f:
				f.write(line)
			self.lastSaveTime = time.time()
			print(time.time())

	def getLitersPer100(self):
		if (self.drivenDistance != 0):
			return self.fuelUsed / (self.drivenDistance/100)
		else:
			return 0.0
	def setSpeed(self, speed):
		if (speed != self.lastSpeed):
			
			currentTime = time.time() #get time
			elapsedTime = currentTime - self.speedUpdateTime
			self.speedUpdateTime = currentTime
			self.drivenDistance += self.lastSpeed * elapsedTime / 3600

			self.lastSpeed = speed

		self.save()

	def setFuel(self, fuel):
		if (fuel > self.lastFuel): #refueled, doesn't affect mpg, but update latest value for future use
			self.lastFuel = fuel
		elif (fuel < self.lastFuel): #lost fuel, convert to liters, and add to total used fuel
			usedPercentage = self.lastFuel - fuel
			usedLiters = usedPercentage / 100 * FUELTANKSIZE
			self.fuelUsed += usedLiters
			self.lastFuel = fuel
		self.save()



"""
calc = LitersPer100()
calc.setSpeed(100)
calc.setFuel(100)

speedAddition = 1
fuel = 100
while True:
	#print(calc.getLitersPer100())
	speedAddition *= -1
	fuel -= 0.0046296295 # % per second, when using 10l/100km
	calc.setSpeed(100+speedAddition)
	calc.setFuel(fuel)
	time.sleep(1)
"""