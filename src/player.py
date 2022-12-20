from src.deck import Deck
from src.hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.value = 0

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
        
