import obd

DEBUG = True

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
			

			self.connection.watch(obd.commands.TIMING_ADVANCE)
			self.connection.watch(obd.commands.ENGINE_LOAD)
			self.connection.watch(obd.commands.COOLANT_TEMP)
			self.connection.watch(obd.commands.CATALYST_TEMP_B1S1)
			self.connection.watch(obd.commands.EVAPORATIVE_PURGE)



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
		elif (label == "timingadvance"):
			if (DEBUG):
				return "10"
			else:
				advance = self.connection.query(obd.commands.TIMING_ADVANCE)
				return (str(advance.value.magnitude))
		elif (label == "coolanttemperature"):
			if (DEBUG):
				return "-"
			else:
				coolant = self.connection.query(obd.commands.COOLANT_TEMP)
				return str(coolant.value.magnitude)
		elif (label == "catalysttemperature"):
			if (DEBUG):
				return "10"
			else:
				temp = self.connection.query(obd.commands.CATALYST_TEMP_B1S1)
				return str(temp.value.magnitude)
		elif (label == "intaketemperature"):
			if (DEBUG):
				return "-"
			else:
				intake = self.connection.query(obd.commands.INTAKE_TEMP)
				return str(intake.value.magnitude)
		elif (label == "engineload"):
			if (DEBUG):
				return "50"
			else:
				load = self.connection.query(obd.commands.ENGINE_LOAD)
				loadint = int(load.value.magnitude)
				return str(loadint)

		elif (label == "evaporativepurge"):
			if (DEBUG):
				return "50"
			else:
				purge = self.connection.query(obd.commands.EVAPORATIVE_PURGE)
				purgeint = int(purge.value.magnitude)
				return str(purgeint)



		return "test"