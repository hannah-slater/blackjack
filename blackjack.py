from src.deck import Deck
from src.card import Card
from src.hand import Hand

def play():
    deck = Deck()
    deck.shuffle()

    #Hands
    playerHand = Hand()
    dealerHand = Hand()

    #Dealer draw:
    dealerHand.addCard(deck.draw())
    dealerHand.addCard(deck.draw())
    dealerValue = dealerHand.getValue()
    print(dealerHand.displayCards())
    print("Value of dealer hand:",dealerValue)

    #Player draw:
    playerHand.addCard(deck.draw())
    playerHand.addCard(deck.draw())
    playerValue = playerHand.getValue()
    print(playerHand.displayCards())
    print("Value of Hand:",playerValue)
    
    #Player given options 'Hit' or 'Stick' (buttons)
    while playerValue < 21:
        i = input("Hit or Stand?\n")
        #if Hit player recieves another card and value is updated
        if i.lower() == "hit":
            playerHand.addCard(deck.draw())
            playerValue = playerHand.getValue()
            print(playerHand.displayCards())
            print("Value of Hand:",playerValue)
        elif i.lower() == "stand":
            break


    #dealer turn
    if playerValue <= 21:
        while dealerValue < playerValue:
            dealerHand.addCard(deck.draw())
            dealerValue = dealerHand.getValue()
            print(dealerHand.displayCards())
            print("Value of dealer hand:",dealerValue)
        if playerValue > dealerValue or dealerValue > 21:
            print("WIN")
        elif playerValue == dealerValue:
            print("DRAW")
        elif dealerValue > playerValue:
            print("LOSE")
    else:
        print("BUST")



if __name__ == '__main__':
    play()
