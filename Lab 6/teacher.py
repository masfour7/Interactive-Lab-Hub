import paho.mqtt.client as mqtt
import uuid
import json

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

topic = "IDD/teacher_student"

# stars cap at 6
student_dict = {}
student_dict['name'] = 'student'
student_dict['stars'] = 0

while True:
        print(f"now writing to topic {topic}")
        print("type new-topic to swich topics")
        while True:
            val = input(">> press anything to add one star to student, press q to quit: ")
            if val =='q':
                exit(0)
            else:
                student_dict['stars'] = (student_dict['stars'] + 1) % 6
                client.publish(topic, json.dumps(student_dict))