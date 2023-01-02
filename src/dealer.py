from src.deck import Deck
from src.hand import Hand
from src.player import Player

#Dealer is a subclass of player
class Dealer(Player):
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.value = 0
        self.final = False

    #Creates a hand for player given the deck
    def createHand(self, deck):
        self.hand.addCard(deck, 2)
        self.value = self.hand.getValue()

    #Plays dealers hand according to the rules set
    def playHand(self, deck, rule):
        while self.value < 17 and self.final == False:
            cards = self.hand.getCards()
            values = [c.getValue() for c in cards]
            if 1 in values and self.value == 17:
                print("Soft 17, rule being applied")
                if rule:
                    self.hit(deck)
                    self.display()
                elif rule == False:
                    self.final = True
            else:
                self.hit(deck)
                self.display()

    #Displays the cards and value of the dealer's hand
    def display(self):
        print("DEALER's HAND\n{}".format(self.hand.displayCards()))
        print("Value of Hand: {}\n".format(self.value))  

    #Evaluates a given player's outcome
    def evaluate(self, player):
        v = player.getValue()
        if v > 21:
            return("BUST")
        elif player.fiveCards() == True:
            player.addWinnings()
            return("WIN")
        elif self.value > 21:
            player.addWinnings()
            return("WIN")
        elif v > self.value:
            player.addWinnings()
            return("WIN")
        elif v == self.value:
            player.draw()
            return("DRAW")  
        elif v < self.value:
            return("LOSE")
        else:
            return("ERROR")