import obd

DEBUG = False

class CarConnection():
	def __init__(self):
		

		if (not DEBUG):
			self.connection = obd.Async(fast=False) #"/dev/ttyUSB0", 

			# everything that was accessible from my car
			self.connection.watch(obd.commands.SPEED)
			self.connection.watch(obd.commands.RPM)
			self.connection.watch(obd.commands.FUEL_LEVEL)
			self.connection.watch(obd.commands.COOLANT_TEMP)
			self.connection.watch(obd.commands.INTAKE_TEMP)
			self.connection.watch(obd.commands.THROTTLE_POS)

			self.connection.start() 


		
		self.rpm = 0

		self.throttle = 0

		self.steeringAngle = 0

		self.speed = 0

	def getValue(self, label):
		if (label == "rpm"):
			if (DEBUG):
				return "3000"

			else:
				rpm = self.connection.query(obd.commands.RPM)
				if (rpm.value != None):
					self.rpm = int(rpm.value.magnitude)
					return str(self.rpm)
		elif (label == "gear"):
			return "1"
		elif (label == "speed"):
			if (DEBUG):
				return "50"
			else:
				speed = self.connection.query(obd.commands.SPEED)
				if (speed.value != None):
					self.speed = int(speed.value.magnitude)
					return str(self.speed)
		elif (label == "fuelpercentage"):
			if (DEBUG):
				return "100"
			else:
				fuel = self.connection.query(obd.commands.FUEL_LEVEL)
				self.fuel = fuel.value.magnitude
				return round(self.fuel, 1)

		elif (label == "throttle"): #percentages
			if (DEBUG):
				return "50"
			else:
				throttle = self.connection.query(obd.commands.THROTTLE_POS)
				if (throttle.value != None):
					self.throttle = throttle.value.magnitude
					resultThrottle = int(self.throttle)
					return str(resultThrottle)

		elif (label == "steering"):
			return str(self.steeringAngle)
		elif (label == "ambienttemperature"):
			return "-"
		elif (label == "coolanttemperature"):
			if (DEBUG):
				return "-"
			else:
				coolant = self.connection.query(obd.commands.COOLANT_TEMP)
				return str(coolant.value.magnitude)
		elif (label == "oiltemperature"):
			return "-"
		elif (label == "intaketemperature"):
			if (DEBUG):
				return "-"
			else:
				intake = self.connection.query(obd.commands.INTAKE_TEMP)
				return str(intake.value.magnitude)



		return "test"