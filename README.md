# CarInfo
Pulling real time data from a Vectra c to a raspberry pi GUI app
Shows various diagnostic/temperature data, speed, rpm, throttle position etc.
Also calculates fuel economy and remaining range of the current fuel tank, this functionality didn't previously exist in this car. 
Fuel economy can be stored on disk.



![Alt text](example.png?raw=true "Example of the interface")

*Setup*
* sudo adduser $USER dialout, log back in again to take effect
* in carconnection.py, set flag DEBUG to: true, for use with a car, false, for offline use
* in main.py modify pygame.display.set_mode, if intending to use in full screen mode
* Connect a elm327 device to the vehicle and pc

*Modifying*
This can probably be modified to work with most cars without gui changes, might require changes to the carconnection.py file
