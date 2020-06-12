import obd

DEBUG = False

class CarConnection():
	def __init__(self):
		

		if (not DEBUG):
			self.connection = obd.Async(fast=False) #"/dev/ttyUSB0", 
			self.connection.watch(obd.commands.RPM)
			self.connection.start() 


		
		self.rpm = 0
		self.rpmAddition = 30

		self.throttle = 0
		self.throttleaddition = 1

		self.steeringAngle = 0
		self.steeringAddition = 1

		self.speed = 0
		self.speedAddition = 1

	def getValue(self, label):
		if (label == "rpm"):
			if (DEBUG):
				self.rpm += self.rpmAddition
				if (self.rpm >= 8000 or self.rpm <= 0):
					self.rpmAddition *= -1
				return str(self.rpm)
			else:
				rpm = self.connection.query(obd.commands.RPM)
				if (rpm.value != None):
					self.rpm = int(rpm.value.magnitude)
					return str(self.rpm)
		elif (label == "gear"):
			return "1"
		elif (label == "speed"):
			self.speed += self.speedAddition
			if (self.speed >= 150 or self.speed <= 0):
				self.speedAddition *= -1
			return str(self.speed)
		elif (label == "fuelpercentage"):
			return "100"
		elif (label == "throttle"): #percentages
			self.throttle += self.throttleaddition
			if (self.throttle >= 100 or self.throttle <= 0):
				self.throttleaddition *= -1
			return str(self.throttle)
		elif (label == "steering"):
			self.steeringAngle += self.steeringAddition
			if (self.steeringAngle >= 100 or self.steeringAngle <= -100):
				self.steeringAddition *= -1
			return str(self.steeringAngle)
		elif (label == "ambienttemperature"):
			return "10"
		elif (label == "coolanttemperature"):
			return "11"
		elif (label == "oiltemperature"):
			return "12"
		elif (label == "intaketemperature"):
			return "13"
		return "test"