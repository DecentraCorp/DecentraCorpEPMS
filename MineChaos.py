#!/usr/bin/env python
# Uses floating inputs on GPIO4, GPIO17, and GPIO22 to generate truly rand$
# Outputs to GPIO 25 when a new number is done and sends the number to STD$

import RPi.GPIO as GPIO
from time import sleep
from EPMS import mineUseBlock
import json
from web3 import Web3, HTTPProvider

GPIO.setmode(GPIO.BCM)

with open("contracts/ChaosCasino.json") as f:
    info_json = json.load(f)
CPabi = info_json["abi"]


w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
#this should connect to the local parity node running the PoA network
#will probably need two seperate web3 instances, one for each network when$
w3.eth.defaultAccount = w3.eth.accounts[0]
repAdd = w3.eth.accounts[0]

add = Web3.toChecksumAddress('0x1fa57e5c672c8b95046ccba214e66ad90160fefa')

ChaosCasino = w3.eth.contract(address=add, abi=CPabi)


sndr = {'from': repAdd}

def detectChaos(pin1, pin2, pin3, tts):  # gets a random set of bits, XORs$
    bit1 = 0
    bit2 = 0
    bit3 = 0
    bitv = 0
    GPIO.setup(pin1, GPIO.IN)
    GPIO.setup(pin2, GPIO.IN)
    GPIO.setup(pin3, GPIO.IN)
    sleep(tts)  # Sleep so the CPU can mess around and change the EMF envi$
    bit1 = GPIO.input(pin1)
    if bit1:
        bit1 = 1
    else:
        bit1 = 0
        sleep(tts)  # Sleep so the CPU can mess around and change the EMF $
        bit2 = GPIO.input(pin2)
    if bit2:
        bit2 = 1
    else:
        bit2 = 0
        sleep(tts)  # Sleep so the CPU can mess around and change the EMF $
        bit3 = GPIO.input(pin3)
    if bit3:
        bit3 = 1
    else:
        bit3 = 0
    # Now do some XOR logic
    bitv = bit1 ^ bit2
    out = bitv ^ bit3
    return out

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

def setEntropyUnit(_entUnit):
    ChaosCasino.functions.setRandomNum(_entUnit).transact(sndr)

while True:
    entropyUnit = getEntropy(64, 4, 17, 22, 0.01)
    print(entropyUnit)
    setEntropyUnit(entropyUnit)
    mineUseBlock()
    sleep(30)
