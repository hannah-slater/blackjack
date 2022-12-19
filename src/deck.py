from src.card import Card

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
    def show(self):
        for c in self.cards:
            print(c.getCard())
            
    #def shuffle(self):
        
    #def draw(self):
        
