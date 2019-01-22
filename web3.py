import json
from GPIO_RNG.py import getEntropy
import time
from web3 import Web3, HTTPProvider
from './contracts/CryptoPatentBlockchain.json' import CryptoPatent
from './contracts/ChaosCasino.json' import ChaosCasino

CPaddress = [CryptoPatent.networks[3].address]
CPabi = [CryptoPatent.abi]
Chaosaddress = [ChaosCasino.networks[3].address]
Chaosabi = [ChaosCasino.abi]


w3 = Web3(HTTPProvider([https://localhost:8545]))
#this should connect to the local parity node running the PoA network
#will probably need two seperate web3 instances, one for each network when building CIB
w3.eth.defaultAccount = w3.eth.accounts[0]

CPB = w3.eth.contract(CPabi, CPaddress)
ChaosCasino = w3.eth.contract(Chaosabi, Chaosaddress)

def mineUseBlock():
    CPB.functions.generateUseBlockWeight().call()

def setEntropyUnit():
    EU = getEntropy(64, 4, 17, 22, 0.01)
    ChaosCasino.functions.setRandomNum(EU).call

#**
#example contract function call
#def check_whether_address_is_approved(address):
#
#**    return contract.functions.isApproved(address).call()
