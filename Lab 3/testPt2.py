import time
import board
# import adafruit_mpu6050
from adafruit_msa3xx import MSA311
from vosk import Model, KaldiRecognizer
import subprocess
import os
import wave
import json
import board
import random


cactus = {"tempmin":7, "tempmax":40, "bloom":False, "friend":True, "oxygen":True, "water":"small cup every ten days"}
airplant = {"tempmin":10, "tempmax":32, "bloom":True,"friend":False, "oxygen":True, "water":"spray water every three days"}
orchid = {"tempmin":15, "tempmax":26, "bloom":True,"friend":False, "oxygen":False, "water":"three ice cubes per week"}
sunflower = {"tempmin":8, "tempmax":34, "bloom":True,"friend":True, "oxygen":False, "water":"large cup every week"}
plant_dic = {"cactus": cactus, "airplant": airplant, "orchid": orchid, "sunflower": sunflower}



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
    subprocess.call("arecord -D hw:1,0 -f cd -c1 -r 16000 -d 5 -t wav recorded_mono.wav" + user_word, shell=True)

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


speak("Hi, ")
while True:
    record_user_word()
    plant = recognize('["cactus airplant orchid sunflower", "[unk]"]')
    if plant != "":
        speak("I’m finally over my identity crisis.")
        if "cactus" in plant:
            plant = "cactus"
            speak("I am a cactus, the ideal temperature for me to live is seven to fourty celsius degrees with direct and ample sunlight. I get thirsty every ten days, and I usually drink a small cup of water every time.") 
            speak("You will most likely not see me bloom. I will be your roommate for almost forever if you are taking good care of me")
        elif "airplant" in plant:
            plant = "airplant"
            speak("I am an airplant, the ideal temperature for me to live is ten to thirty-two celsius degrees with no direct sunlight. You can just spray water on me three times a week in the morning.") 
            speak("I only bloom once in my life, most likely in summer. I will be your roommate for around a year if you are taking good care of me")
        elif "orchid" in plant:
            plant = "orchid"
            speak("I am an orchid, the ideal temperature for me to live is fifteen to twenty-six celsius degrees with indirect sunlight. Three ice cubes every week will be enough drink for me.") 
            speak("I am blooming all the time. I will be your roommate for fifteen to twenty years if you are taking good care of me")
        elif "sunflower" in plant:
            plant  = "sunflower"
            speak("I am a sunflower, the ideal temperature for me to live is eight to thirty-four celsius degrees with direct and ample sunlight. I get thirsty every week, and I usually drink a large cup of water every time.") 
            speak("You will see me bloom in July for at least eight weeks if you are taking good care of me")
        
        break
    wrong_mess()
    speak("You still there?")


speak("Also, I’m not sure where I feel most comfortable growing. Now could you move me around to different places, and say 'done' when you’re done?")
while True:
    record_user_word()
    result = recognize('["done wait", "[unk]"]')
    if "wait" in result:
        speak("Ok, let me know when you're done.")
        time.sleep(3)
    elif "done" in result:
        break
    wrong_mess()
    speak("You still there?")


i2c = board.I2C()  # uses board.SCL and board.SDA
# mpu = adafruit_mpu6050.MPU6050(i2c)
msa = MSA311(i2c)
while True:
    temp = msa.temperature
    
    print(plant)
    print(plant in plant_dic)

    if plant in plant_dic:
        min = plant_dic[plant]["tempmin"]
        max = plant_dic[plant]["tempmax"]
        if temp >= min and temp <= max:
            speak("This is a great place! I love the temperature and sunlight here!")
            break
    
        speak("Umm, try somewhere else. Here the temperature is degree but my ideal temp is from" +min + "degree to" + max + "degree")
        speak("Let me know when you are done.") 
        while True:
            record_user_word()
            result = recognize('["done", "[unk]"]')
            if "done" in result:
                break


speak("Now feel free to ask me some questions")
while True:
    speak("Hi, please ask")
    record_user_word()
    result = recognize('["water friend temperature", "[unk]"]')
    if "water" in result or "watering" in result:
        wat = plant_dic[plant]["water"]
        response = ["I do not need water for now","I need water now."]
        ran = random.randint(0,len(response)-1)
        line = response[ran]
        speak(line +"My watering preference is" + wat)
    elif "friend" in result or "lonely" in result:
        company = plant_dic[plant]["friend"]
        if company == True:
            speak("Yes,it will be great if you can find me a friend.")
        else:
            speak("No. I just love to be the only child here.")
    elif "temperature" in result or "sunbathing" in result:
        temp = msa.temperature
        min = plant_dic[plant]["tempmin"]
        max = plant_dic[plant]["tempmax"]
        if temp >= min and temp <= max:
            speak("This is a great place! I love the temperature and sunlight here!")
        else:
            speak("Umm, try somewhere else. Here the temperature is" + temp + "degree but my ideal temp is from" +min + "degree to" + max + "degree")
    elif "bug" in result:
        response = ["I have bugs on me please help","I am doing great thank you."]
        ran = random.randint(0,len(response)-1)
        line = response[ran]
        speak(line)

    speak("Any more questions?")
    record_user_word()
    result = recognize('["yes no", "[unk]"]')
    if "yes" in result:
        break
    if "no" in result:
        speak("Thanks! I am going to rest for now")