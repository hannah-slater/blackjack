from src.card import Card

class Hand:
    def __init__(self):
        self.cards = []

    #adds a card object to the hand
    def addCard(self, card):
        self.cards.append(card)
        self.calculateValue()

    #returns a string containg the cards present in the hand
    def displayCards(self):
        string = ""
        for card in self.cards:
            string += card.getCard() + "\n"
        return string

    #calculates the value of the hand
    def calculateValue(self):
        value = 0
        #holds the value of the amount of aces in the hand
        ace = 0
        
        for card in self.cards:
            v = card.getValue()
            if v == 1:
                ace += 1
            else:
                value += v
        
        #evaluates the value of aces if there are one or more in the hand
        if ace != 0:
            while ace >= 2:
                value += 1
                ace -= 1

            if ace == 1:
                if (value + 11) <= 21:
                    value += 11
                else:
                    value += 1
        self.handValue = value

    #returns the value of the hand
    def getValue(self):
        return self.handValue
