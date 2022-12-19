from src.deck import Deck
from src.card import Card

def play():
    deck = Deck()
    #deck.shuffle()

    #Player draw:
    a = deck.draw()
    b = deck.draw()
    print(calcValue(a,b))

    #Dealer draw:
    c = deck.draw()
    d = deck.draw()
    print(calcValue(c,d))
    
    #Player given options 'Hit' or 'Stick' (buttons)
    #if Hit player recieves another card and value is updated

    #if stick, dealer plays by house rules

    #Win/Loss decided
    #play next round?

def calcValue(c1, c2):
    #add in ace rules
    
    value = c1.getValue() + c2.getValue()
    return value

if __name__ == '__main__':
    play()
