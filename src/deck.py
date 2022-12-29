from src.card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    #Builds a standard deck of cards
    def build(self):
        for suit in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            self.cards.append(Card(suit, "Ace", 1))
            for card in range(2,11):
                self.cards.append(Card(suit,card,card))
            for pictureCard in ["Jack","Queen","King"]:
                self.cards.append(Card(suit, pictureCard, 10))

    #Shuffles the deck into a random order      
    def shuffle(self):
        shuffledCards = []
        cards = [*range(1,53)]
        for i in range(1,53):
            r = random.randint(1,53)
            if r in cards:
                shuffledCards.append(self.cards[r-1])
                cards.remove(r)
        self.cards = shuffledCards

    #Returns and removes a card from the end of the list
    def draw(self):
        return self.cards.pop()
        
