from src.card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def getCards(self):
        return self.cards

    def displayCards(self):
        string = ""
        for card in self.cards:
            string += card.getCard()
        return string

    def getValue(self):
        value = 0
        for card in self.cards:
            a = card.getValue()
            value += a
        return value
