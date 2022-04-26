from brownie import *
import time


class Player:
    def __init__(self, contract, payDic, me):
        self.contract = contract
        self.payDic = payDic
        self.me = me
        self.lastCheck = int(time.time())
        self.factor = 100
        self.balance = 0
        self.gold = 0
        self.dark = 0
        self.goldCollectors = 0
        self.darkCollectors = 0
        self.multiplier = 0
        self.win = False

    def buyLand(self):
        try:
            self.contract.buyLand({"from": self.me, "value": Wei("1 ether")})
            self.lastCheck = int(time.time())
            self.state()
            self.balances()
        except:
            return 0

    def buyGold(self):
        try:
            self.contract.buyGold(self.payDic)
            self.state()
            self.balances()
        except:
            return 0

    def buyDark(self):
        try:
            self.contract.buyDark(self.payDic)
            self.state()
            self.balances()
        except:
            return 0

    def buyGoldCollector(self):
        try:
            self.contract.buyGoldCollector(self.payDic)
            self.state()
            self.balances()
        except:
            return 0

    def buyDarkCollector(self):
        try:
            self.contract.buyDarkCollector(self.payDic)
            self.state()
            self.balances()
        except:
            return 0

    def upgradeMultiplier(self):
        try:
            self.contract.upgradeMultiplier(self.payDic)
            self.state()
            self.balances()
        except:
            return 0

    def display(self):
        self.balances()
        return self.balance, self.gold, self.dark, self.goldCollectors, self.darkCollectors, self.multiplier

    def state(self):
        try:
            self.contract.refresh()
            self.lastCheck = int(time.time())
            res = self.contract.display().return_value
            self.balance = str(round(float(self.me.balance().to("ether")), 4))
            self.gold = int(res[0])/self.factor
            self.dark = int(res[1])/self.factor
            self.goldCollectors = int(res[2])
            self.darkCollectors = int(res[3])
            self.multiplier = int(res[4])
        except:
            self.balance = str(round(float(self.me.balance().to("ether")), 4))
            self.gold = 0
            self.dark = 0
            self.goldCollectors = 0
            self.darkCollectors = 0
            self.multiplier = 0

    def balances(self):
        new_check = int(time.time())
        remainder = new_check - self.lastCheck
        if self.gold >= 100000 and self.dark >= 10000 and self.goldCollectors >= 10 and self.darkCollectors >= 10:
            self.win = True
            self.state()
            return
        if remainder < 1:
            return
        self.lastCheck = new_check
        self.gold += remainder * self.goldCollectors * self.multiplier
        self.dark += (remainder * self.darkCollectors * self.multiplier) / 4
