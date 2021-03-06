#!/usr/bin/python3
# Uses floating inputs on GPIO4, GPIO17, and GPIO22 to generate truly rand$
# Outputs to GPIO 25 when a new number is done and sends the number to STD$
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

def mineUseBlock():
    print(repAdd)
    CPB.functions.generateUseBlockWeight().transact(sndr)




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
