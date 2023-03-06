import json
import configparser
from web3 import Web3


class Blockchain:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        self.url = ("http://127.0.0.1:7545")
        self.web3 = Web3(Web3.HTTPProvider(self.url))
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.abi = json.loads(config['ABI']['abi_structure'])
        self.abi_address = "0xcD5560F19e79B02338405deD2ecd2CC6022e3784"
        self.contract = self.web3.eth.contract(address=self.abi_address, abi=self.abi)

    def calculate(self, a, b, operator):
        if operator == '+':
            return self.contract.functions.add(a, b).call()
        elif operator == '-':
            return self.contract.functions.subtract(a, b).call()
        elif operator == '*':
            return self.contract.functions.multiply(a, b).call()
        elif operator == '/':
            return self.contract.functions.divide(a, b).call()
        else:
            return "Invalid operator"