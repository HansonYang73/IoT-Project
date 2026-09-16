import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

BLUE_LED = 1
RED_LED = 2
BUZZER = 3

GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

def success():
    GPIO.output(BLUE_LED, GPIO.HIGH)
    sleep(3)
    GPIO.output(BLUE_LED, GPIO.LOW)

def failure():
    GPIO.output(RED_LED, GPIO.HIGH)
    GPIO.output(BUZZER, GPIO.HIGH)
    sleep(3)
    GPIO.output(RED_LED, GPIO.LOW)
    GPIO.output(BUZZER, GPIO.LOW)
    