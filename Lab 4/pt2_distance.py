"""
	Reading distance from the laser based VL53L1X
	This example prints the distance to an object. If you are getting weird
	readings, be sure the vacuum tape has been removed from the sensor.
"""

import qwiic
import time

import time
import board
import board
from adafruit_apds9960.apds9960 import APDS9960

from vosk import Model, KaldiRecognizer
import subprocess
import os
import wave
import json
import board
import random

def speak(instruction):
    command = """
    echo {} | festival --tts
    """.format(instruction)
    subprocess.call(command, shell=True)

print("VL53L1X Qwiic Test\n")
ToF = qwiic.QwiicVL53L1X()
if (ToF.sensor_init() == None):					 # Begin returns 0 on a good init
	print("Sensor online!\n")

while True:
	try:
		ToF.start_ranging()						 # Write configuration bytes to initiate measurement
		time.sleep(.005)
		distance = ToF.get_distance()	 # Get the result of the measurement from the sensor
		time.sleep(.005)
		ToF.stop_ranging()

		distanceInches = distance / 25.4
		distanceFeet = distanceInches / 12.0

		print("Distance(mm): %s Distance(ft): %s" % (distance, distanceFeet))
		if(distance > 200):
			speak("You are far")
		elif(distance > 100 and distance < 200):
			speak("almost there")
		elif(distance < 100):
			speak("you found me! Congrats!")
		time.sleep(1)


	except Exception as e:
		print(e)