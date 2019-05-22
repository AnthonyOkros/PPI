#!/usr/bin/python3
# Script created by Anthony Okros.
# Ensure gps3 is installed using: sudo -H pip3 install gps3
# Visit https://pypi.org/project/gps3/ for more information

import board
import neopixel
from gps3 import gps3
import time

# Setting up NeoPixel attributions
num_pixels = 64
pixel_pin = board.D10
# Declaring NeoPixel attributes to "pixels" variable
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
# Setting NeoPixel brightness to 0.01 so we dont get blind
pixels.brightness = 0.01

# Setting up rainbow function goodness so can be called when times are not exciting       
def rainbow_cycle():
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.show()
        time.sleep(1)

# Used for the rainbow function i think?
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# Where the magic happens
while True:
  # Assigning RGB color values to variables to use later
  RED = (255, 0, 0)
  YELLOW = (255, 150, 0)
  GREEN = (0, 255, 0)
  CYAN = (0, 255, 255)
  BLUE = (0, 0, 255)
  PURPLE = (180, 0, 255)
  OFF = (0, 0, 0)
  # Setting up GPS socket and connection using gps3 library for gpsd  
  gps_socket = gps3.GPSDSocket()
  data_stream = gps3.DataStream()
  gps_socket.connect()
  gps_socket.watch()
  # Creating variable "new_data" to capture line data from Ublox GPS module
  for new_data in gps_socket:
    if new_data:
        # Unpack data, specifically the "speed" attribute captured from Ublox GPS module
        data_stream.unpack(new_data)
        speed = data_stream.TPV['speed']   
        # The first line of data presented is of string ("n/a"), so we cannot compare this 
        # data type of string to a float. So we must run the script, and wait until float 
        # data type values are captured.
        if speed == "n/a":
          print(speed)
        # Declare data to be float so that data types are the same and can be compared.  
        else:
          speed = float(speed)  
          # Declare threshold: if below a speed of 1.000, then consider the BitBall to be
          # stationary and thus turn off NeoPixels.
          if float(speed) < 1.000:
            print ("i am not really moving")
            pixels.fill(OFF)
          # If moving continue and assign colors to certain values. The smaller (slower)
          # the speed the cooler the color. The larger (faster) the speed the warmer the 
          # color.  
          else:
            if 1.000 < float(speed) < 2.000: # Check value captured, if between 1 and 2
              pixels.fill(CYAN) # Display color CYAN on NeoPixels
              pixels.show()
              print ("around 1.5")
              print (speed)
            if 2.000 < float(speed) < 3.000:
              pixels.fill(BLUE)
              #pixels.show()
              print ("around 2.5")
              print (speed)
            if 3.000 < float(speed) < 4.000:
              pixels.fill(PURPLE)
              #pixels.show()
              print ("around 3.5")
              print (speed)
            if 4.000 < float(speed) < 5.000:
              pixels.fill(YELLOW)
              #pixels.show()
              print ("around 4.5")
              print (speed)
            if 5.000 < float(speed) < 6.000:
              pixels.fill(RED)
              #pixels.show()
              print ("around 5.5")
              print (speed)
            time.sleep(1) # Run loop every 1 second

