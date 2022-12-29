from src.deck import Deck
from src.hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.value = 0
        self.money = 100
        self.wager = 0
        self.five = False

    #Creates a hand for player given the deck
    def createHand(self, deck):
        self.hand.addCard(deck, 2)
        self.value = self.hand.getValue()
  
    #Adds a card to the hand of the player
    def hit(self, deck):
        self.hand.addCard(deck, 1)
        self.value = self.hand.getValue()

    #Returns the value of the players hand
    def getValue(self):
        return self.value

    #Returns name of player
    def getName(self):
        return self.name

    #Returns players hand
    def getHand(self):
        return self.hand

    #Returns money/balance of the player
    def getMoney(self):
        return self.money

    #Sets the players wager for the current round
    def setWager(self, w):
        self.wager = w
        self.money -= w
    
    #Sets the winning variable for if a player has 5 cards to true
    def setFiveCards(self):
        self.five = True
    
    #Returns the variable for if a player has five cards
    def fiveCards(self):
        return self.five

    #Executes if the player draws with the dealer
    def draw(self):
        self.money += self.wager

    #Adds winnings if player wins against the dealer
    def addWinnings(self):
        self.money += 2 * self.wager

    #Clears hand between rounds
    def clearHand(self):
        self.hand.clear()