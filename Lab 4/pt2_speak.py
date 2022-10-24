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

while True:
    speak("I am here")
    time.sleep(2)