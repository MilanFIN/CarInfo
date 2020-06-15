import obd
from obd.protocols import ECU
from obd.utils import bytes_to_int
from time import sleep




connection = obd.Async(fast=False) #"/dev/ttyUSB0", 



connection.watch(obd.commands.SPEED)
connection.watch(obd.commands.RPM)
connection.watch(obd.commands.FUEL_LEVEL)
connection.watch(obd.commands.COOLANT_TEMP)
connection.watch(obd.commands.INTAKE_TEMP)
connection.watch(obd.commands.THROTTLE_POS)






connection.start() # start the async update loop



while True:
	
	throttle = connection.query(obd.commands.THROTTLE_POS)
	if (throttle.value != None):
		print("throttle", throttle.value.magnitude)
	intake = connection.query(obd.commands.INTAKE_TEMP)
	if (intake.value != None):
		print("intake", intake.value.magnitude)

	coolant = connection.query(obd.commands.COOLANT_TEMP)
	if (coolant.value != None):
		print("coolant", coolant.value.magnitude)
	fuel = connection.query(obd.commands.FUEL_LEVEL)
	if (fuel.value != None):
		print("fuel", fuel.value.magnitude)
	speed = connection.query(obd.commands.SPEED)
	if (speed.value != None):
		print("speed", speed.value.magnitude)
	rpm = connection.query(obd.commands.RPM)
	if (rpm.value != None):
		print("rpm", rpm.value.magnitude)
	
	sleep(0.5)
