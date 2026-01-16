from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

servo = kit.servo[0]

servo.angle = 90
time.sleep(2)

servo.angle = 0
time.sleep(2)

servo.angle = 180
time.sleep(2)

servo.angle = 90