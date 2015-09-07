#!/usr/bin/python3

import argparse
import RPi.GPIO as GPIO
import time

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dur", help="set durreation of time the LED is lit", type=float, default=0.5) 
args = parser.parse_args()

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, True)

time.sleep(args.dur)

GPIO.output(21, False)
GPIO.cleanup()
