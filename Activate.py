#!/usr/bin/python3



import json
from web3 import Web3, HTTPProvider


with open("contracts/CryptoPatentBlockchain.json") as f:
    info_json = json.load(f)
CPabi = info_json["abi"]


w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
#this should connect to the local parity node running the PoA network
#will probably need two seperate web3 instances, one for each network when$
w3.eth.defaultAccount = w3.eth.accounts[0]
repAdd = w3.eth.accounts[0]

add = Web3.toChecksumAddress('0x24e2b4690BDBdA1A7488842c2F3c5cCd306bE617')

CPB = w3.eth.contract(address=add, abi=CPabi)


sndr = {'from': repAdd}

userName = input("Enter Your DecentraCorp User Name: ")
password = input("Enter Your DecentraCorp Password: ")

_userId = userName + password



def activateReplication():
    print(repAdd)
    CPB.functions.generateReplicationBlock(1, repAdd, _userId).transact(sndr)

activateReplication()
