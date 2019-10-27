from Rass import *
from time import sleep
from time import time
rass = Rass()

# setting up the ultrasonic sensor
inPin = 23
outPin = 24
GPIO.setup(inPin, GPIO.IN)
GPIO.setup(outPin, GPIO.OUT)

GPIO.output(outPin, False)
sleep(2)

def get_distance():
    GPIO.output(outPin, True)
    sleep(0.00001)
    GPIO.output(outPin, False)
    while(GPIO.input(inPin)) == 0:
        pulse_start = time()
    while(GPIO.input(inPin)) == 1:
        pulse_end = time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print(distance)

for i in range(100):
    get_distance()
    sleep(1)
