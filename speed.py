#!/usr/bin/python3

import gpsd
import time
# Connect to the local gpsd
gpsd.connect()
# Get location of GPS
packet = gpsd.get_current()

# See speed GOTTA GO FAST and test an if else statement using the speed value
try:
	while True:
		print("Speed: " + str(packet.speed()))
		time.sleep(1)
		if str(packet.speed()) == "0":
			print("correct")
		else:
			print("incorrect")
except KeyboardInterrupt:
        print('Ended Script')

