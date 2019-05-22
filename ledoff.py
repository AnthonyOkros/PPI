#!/usr/bin/python3

import board
import neopixel

pixels = neopixel.NeoPixel(board.D10, 64)

pixels.fill((0, 0, 0))
pixels.brightness = 0.01
