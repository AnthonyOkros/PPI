#!/usr/bin/python3
# Simple test for NeoPixels on Raspberry Pi
import board
import neopixel
import gpsd
import time
# Connect to the local gpsd
gpsd.connect()
# Get location of GPS
packet = gpsd.get_current()

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.

# LED strip configuration:
#LED_COUNT      = 64      # Number of LED pixels.
#LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN       = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
#LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
#LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
#LED_BRIGHTNESS = 2     # Set to 0 for darkest and 255 for brightest
#LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
#LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
#LED_ORDER      = GRB

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
#ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(board.D10, 64)


pixels.brightness = 0.01

# See speed GOTTA GO FAST and test an if else statement using the speed value
def speed():
  print("Speed: " + str(packet.speed()))
  time.sleep(1)
  if str(packet.speed()) == "0":
    print("correct")
  else:
    print("incorrect")

def rainbow(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
          strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
    strip.show()
    time.sleep(wait_ms/1000.0)

try:
  while True:
    speed()
    if str(packet.speed()) < "5":
      pixels.fill((0, 0, 255))
      pixels.show()
    if str(packet.speed()) > "5":
      pixels.fill((255, 0, 0))
      pixels.show()
    if str(packet.speed()) == "0":
      pixels.fill((0, 0, 255))
      pixels.show()
      #rainbow(strip, wait_ms=20, iterations=5)
      #pixels.show()
except KeyboardInterrupt:
  print('Ended Script')


