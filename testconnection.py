import obd
from time import sleep

connection = obd.Async(fast=False) #"/dev/ttyUSB0", 

connection.watch(obd.commands.RPM)

connection.start() # start the async update loop


while True:
	rpm = connection.query(obd.commands.RPM)
	if (rpm.value != None):
		print(rpm.value.magnitude)
	sleep(0.5)