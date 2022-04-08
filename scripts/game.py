from brownie import *
from .pygame_utils import loop
from .tycoon_utils import Player

def main():
    me = a[0]
    payDic = {"from": me}
    contract = Game.deploy(payDic)
    player = Player(contract=contract, payDic=payDic, me=me)
    loop(player)


