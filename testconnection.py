import obd
from obd.protocols import ECU
from obd.utils import bytes_to_int
import obd.utils
from time import sleep


connection = obd.OBD(fast=False) #"/dev/ttyUSB0", 




#r = connection.query(obd.commands.ELM_VERSION)
#print(r.value.magnitude)#str, ELM327 v1.5


#r = connection.query(obd.commands.ELM_VOLTAGE)
#print(r.value.magnitude)#str, 12.0 volt


#ACCELERATOR_POS_D & ACCELERATOR_POS_E


#Commanded equivalence ratio
#r = connection.query(obd.commands.COMMANDED_EQUIV_RATIO)
#print(r.value)#ratio (1.99), float


#absolute load 
#r = connection.query(obd.commands.ABSOLUTE_LOAD)
#print(r.value)#percentages, float

#engine load
#r = connection.query(obd.commands.ENGINE_LOAD)
#print(r.value.magnitude)#float, probably %


#control module voltage, BATTERY???
#r = connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
#print(r.value)# VOLTS, float

#supported pids???
#r = connection.query(obd.commands.PIDS_C)
#print(r.value)#bytearray (01111000110100000000000000000000)



#Catalyst Temperature
#r = connection.query(obd.commands.CATALYST_TEMP_B1S1)
#print(r.value)#degrees Celsius, NEGATIVE???

#evaporative purge
#r = connection.query(obd.commands.EVAPORATIVE_PURGE)
#print(r.value)#evaporative purge??? 0.0%

#engine light travel
#r = connection.query(obd.commands.DISTANCE_W_MIL)
#print(r.value)#distance traveled with MIL on, KM

#timing advance
#r = connection.query(obd.commands.TIMING_ADVANCE)
#print(r.value.magnitude)#degrees


"""

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

"""