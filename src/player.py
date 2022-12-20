from src.deck import Deck
from src.hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.value = 0
        self.money = 100
        self.wager = 0

    def createHand(self, deck):
        self.hand.addCard(deck, 2)
        self.value = self.hand.getValue()

    def hit(self, deck):
        self.hand.addCard(deck, 1)
        self.value = self.hand.getValue()

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def getHand(self):
        return self.hand

    def getMoney(self):
        return self.money

    def getWager(self):
        return self.wager

    def setWager(self, w):
        self.wager = w
        self.money -= w

    def draw(self):
        self.money += self.wager

    def addWinnings(self):
        self.money += 2 * self.wager

    def clearHand(self):
        self.hand.clear()
        
