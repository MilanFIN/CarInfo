import time

FUELTANKSIZE = 60 #liters, opel vectra c = 60

class LitersPer100():
	def __init__(self):
		pass
		self.lastSpeed = 0.0
		self.lastFuel = 0.0


		self.speedUpdateTime = time.time()


		self.drivenDistance = 0.0
		self.fuelUsed = 0.0

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

	def setFuel(self, fuel):
		if (fuel > self.lastFuel): #refueled, doesn't affect mpg, but update latest value for future use
			self.lastFuel = fuel
		elif (fuel < self.lastFuel): #lost fuel, convert to liters, and add to total used fuel
			usedPercentage = self.lastFuel - fuel
			usedLiters = usedPercentage / 100 * FUELTANKSIZE
			self.fuelUsed += usedLiters
			self.lastFuel = fuel


calc = LitersPer100()
calc.setSpeed(100)
calc.setFuel(100)

speedAddition = 1
fuel = 100
while True:
	pass
	print(calc.getLitersPer100())
	speedAddition *= -1
	fuel -= 0.0046296295 # % per second, when using 10l/100km
	calc.setSpeed(100+speedAddition)
	calc.setFuel(fuel)
	time.sleep(1)