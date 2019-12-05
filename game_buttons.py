import RPi.GPIO as GPIO
from time import sleep

redButton = 4
blueButton = 27
greenButton = 22
yellowButton = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(redButton, GPIO.IN)
GPIO.setup(blueButton, GPIO.IN)
GPIO.setup(greenButton, GPIO.IN)
GPIO.setup(yellowButton, GPIO.IN)

while True:
    if GPIO.input(redButton):
        print("red")
        while GPIO.input(redButton):
            #wait for button to release
            sleep(0.001)
    elif GPIO.input(blueButton):
        print("blue")
        while GPIO.input(blueButton):
            #wait for button to release
            sleep(0.001)
    elif GPIO.input(greenButton):
        print("green")
        while GPIO.input(greenButton):
            #wait for button to release
            sleep(0.001)
    elif GPIO.input(yellowButton):
        print("yellow")
        while GPIO.input(yellowButton):
            #wait for button to release
            sleep(0.001)
    else:
        print("Waiting...")
        sleep(0.1)