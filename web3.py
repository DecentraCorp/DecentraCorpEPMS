import json
from GPIO_RNG.py import getEntropy
import time
from web3 import Web3, HTTPProvider
from './contracts/CryptoPatentBlockchain.json' import CryptoPatent
from './contracts/ChaosCasino.json' import ChaosCasino

CPaddress = [CryptoPatent.networks[3636].address]
CPabi = [CryptoPatent.abi]
Chaosaddress = [ChaosCasino.networks[3636].address]
Chaosabi = [ChaosCasino.abi]


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
#this should connect to the local parity node running the PoA network
#will probably need two seperate web3 instances, one for each network when building CIB
w3.eth.defaultAccount = w3.eth.accounts[0]
repAdd = w3.eth.accounts[0]

CPB = w3.eth.contract(CPabi, CPaddress)
ChaosCasino = w3.eth.contract(Chaosabi, Chaosaddress)

async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def mineUseBlock():
    CPB.functions.generateUseBlockWeight().call()

def setEntropyUnit():
    EU = getEntropy(64, 4, 17, 22, 0.01)
    ChaosCasino.functions.setRandomNum(EU).call()

def mineChas():
     block_filter = w3.eth.filter('latest')
        tx_filter = w3.eth.filter('repAdd', 'repWeight')
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(
                asyncio.gather(
                    log_loop(block_filter, 2),
                    log_loop(tx_filter, 2)))
        finally:
            setEntropyUnit()
            mineUseBlock();
            loop.close()

#**
#example contract function call
#def check_whether_address_is_approved(address):
#
#**    return contract.functions.isApproved(address).call()

#**
#example Asynchronous Filter Polling
#import asyncio
#
#
#def handle_event(event):
#    print(event)
#    # and whatever
#
#async def log_loop(event_filter, poll_interval):
#    while True:
#        for event in event_filter.get_new_entries():
#            handle_event(event)
#        await asyncio.sleep(poll_interval)
#
#def main():
#    block_filter = w3.eth.filter('latest')
#    tx_filter = w3.eth.filter('pending')
#    loop = asyncio.get_event_loop()
#    try:
#        loop.run_until_complete(
#            asyncio.gather(
#                log_loop(block_filter, 2),
#                log_loop(tx_filter, 2)))
#    finally:
#        loop.close()
#**
