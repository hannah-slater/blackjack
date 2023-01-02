from src.card import Card
from src.deck import Deck

class Hand:
    def __init__(self):
        self.cards = []
        self.valid = True

    #Adds a card object to the hand
    def addCard(self, deck, n):
        for i in range (1, n+1):
            self.cards.append(deck.draw())
        self.calculateValue()

    #Returns a string containing the cards present in the hand
    def displayCards(self):
        string = ""
        last = 0
        for card in self.cards:
            string += card.getCard()
            last += 1
            if last != len(self.cards):
                string += "\n"
        return string

    #Calculates the value of the hand
    def calculateValue(self):
        value = 0
        
        for card in self.cards:
            v = card.getValue()
            value += v
        
        #Evaluates the value of aces if there are one or more in the hand
        a = self.checkAces()
        if a != 0:
            while a >= 2:
                a -= 1

            if a == 1:
                if (value + 10) <= 21:
                    value += 10
        
        if value >= 22:
            self.valid = False
        self.handValue = value

    def checkAces(self):
        aces = 0
        for card in self.cards:
            v = card.getValue()
            if v == 1:
                aces += 1
        return aces

    #Returns the value of the hand
    def getValue(self):
        return self.handValue

    #Returns card objects
    def getCards(self):
        return self.cards
    
    #Returns valid status
    def getValid(self):
        return self.valid

    #Returns amount of cards in hand
    def amountCards(self):
        return len(self.cards)

    #Clears hand for beginning a new round
    def clear(self):
        self.cards = []

    #Allows test functions to add specific cards to hand
    def addCardTest(self, card):
        self.cards.append(card)
        self.calculateValue()