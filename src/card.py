class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value

    #Returns the card to display to the player
    def getCard(self):
        c = "{} of {}".format(self.name,self.suit)
        return c

    #Returns the value of the card to calculate scores
    def getValue(self):
        return self.value
        
