from tkinter.tix import DECREASING
from brownie import network, accounts, MockV3Aggregator
from web3 import Web3
import time

FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local", "ganache-local2"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.load("dd-test")


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        time.sleep(1)
    print("Mocks deployed!")
