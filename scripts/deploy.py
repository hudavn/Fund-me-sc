from brownie import FundMe, accounts, network, config, MockV3Aggregator
import time
from scripts.helpful import deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        # publish_source=config["network"][network.show_active()].get("verify"),
    )
    time.sleep(1)
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
