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

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

user_word = "recorded_mono.wav"
model = Model("model")

def speak(instruction):
    command = """
    echo {} | festival --tts
    """.format(instruction)
    subprocess.call(command, shell=True)

def wrong_mess():
    speak("What was that? I didn't get it!")

def record_user_word():
    subprocess.call("arecord -D hw:1,0 -f cd -c1 -r 16000 -d 5 -t wav " + user_word, shell=True)

def recognize(pattern):
    wf = wave.open(user_word, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    rec = KaldiRecognizer(model, wf.getframerate(), pattern)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print("Result:", res['text'])
            return res['text']
        # else:
        #     print(rec.PartialResult())
    print("Failed to recognize")
    return ""


#### part 1: identify type of medicine wanted
speak("Hi friend. Great to finally meet you. What symptoms are you having")
while True:
    record_user_word()
    result = recognize('["sneezing cold injury", "[unk]"]')
    if result != "":
        if "sneezing" in result:
            speak("Try to take Clarityn. It is good for sneezing. Hello, I am Clarityn")
        elif "injury" in result:
            speak("Try to take Bandaid. It is good for injury. Hello, I am bandaid")
        elif "cold" in result:
            speak("Try to take tylenol. It is good for a headache. Hello, I am Tylenol")
        break
    
    wrong_mess()
    speak("Coulnd't hear you. Can you say again?")


#### part 2: where am I
speak("Try to find me. I will tell you when you are close")

i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

while True:
    prox = apds.proximity

    if(prox == 0):
        speak("You are far")
        time.sleep(3)
    elif(prox > 0 and prox < 100):
        speak("almost there")
        time.sleep(3)
    elif(prox > 100):
        speak("you found me! Congrats!")
        break

#### part 3: ask questions
speak("Now feel free to ask me some questions about medicines you have. Claritin? Tylenol? or BandAid?")
while True:
    record_user_word()
    medicine = recognize('["claritin tylenol bandaid", "[unk]"]')
    if medicine != "":
        speak("Thanks! let me transfer you to that medicine. It will tell you more about itslef")
        if "claritin" in medicine:
            medicine = "claritin"
            speak("I am a claritin, used for relief of sneezing, runny nose, watery eyes, and itchy throat") 
            speak("you can take one of me per day")
        elif "tylenol" in medicine:
            medicine = "tylenol"
            speak("I am a tylenol, used for common cold, toothache, backache, and headache") 
            speak("you can take one of me every 6 hours")
        elif "bandaid" in medicine:
            medicine  = "bandaid"
            speak("I am a bandaid, used for minor cuts and scrapes") 
            speak("you can use me whenever you want")

        
        break

    speak("Any more questions?")

    record_user_word()
    result = recognize("yes no")
    if "yes" in result:
        break
    if "no" in result:
        speak("Thanks! I am going to rest for now")