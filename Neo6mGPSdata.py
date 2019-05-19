#!/usr/bin/python3

import gpsd
import time
# Connect to the local gpsd
gpsd.connect()

# Connect somewhere else
#gpsd.connect(host="127.0.0.1", port=2947)

# Get gps position
packet = gpsd.get_current()

# See the inline docs for GpsResponse for the available data
# print(packet.position())

# See amount of satelluts connected
# print("Satellites: " + str(packet.sats))

# See speed GOTTA GO FAST
try:
	while True:
		print("Speed: " + str(packet.speed()))
		time.sleep(1)
except KeyboardInterrupt:
        print('Ended Script')

