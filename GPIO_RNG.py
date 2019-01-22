#!/usr/bin/env python
# Uses floating inputs on GPIO4, GPIO17, and GPIO22 to generate truly random numbers
# Outputs to GPIO 25 when a new number is done and sends the number to STDOUT

import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)


def detectChaos(pin1, pin2, pin3, tts):  # gets a random set of bits, XORs them, and outputs one random bit
    bit1 = 0
    bit2 = 0
    bit3 = 0
    bitv = 0
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.IN)
    GPIO.setup(pin3, GPIO.IN)
    sleep(tts)  # Sleep so the CPU can mess around and change the EMF environment
    bit1 = GPIO.input(pin1)
    if bit1:
        bit1 = 1
    else:
        bit1 = 0
        sleep(tts)  # Sleep so the CPU can mess around and change the EMF environment
        bit2 = GPIO.input(pin2)
    if bit2:
        bit2 = 1
    else:
        bit2 = 0
        sleep(tts)  # Sleep so the CPU can mess around and change the EMF environment
        bit3 = GPIO.input(pin3)
    if bit3:
        bit3 = 1
    else:
        bit3 = 0
    # Now do some XOR logic
    bitv = bit1 ^ bit2
    out = bitv ^ bit3
    return out


# get an x-bit number by looping through a string a bunch. Pin4 is LEDout.
def getEntropy(x, pin1, pin2, pin3, tts=0.01):
    binstr = ''  # Set up to be converted to binary
    rint = 0
    rbit = 0
    i = 0
    for i in range(0, x-1):
        i += 1
        rbit = detectChaos(pin1, pin2, pin3, tts)
        binstr = binstr + str(rbit)
    rint = int(binstr, 2)
    return rint


while True:
    print(getEntropy(64, 4, 17, 22, 0.01))  # bits, in1, in2, in3, out, tts
