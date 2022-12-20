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
    print("DEALERS HAND\n"+dealerHand.displayCards())
    print("Value of dealer hand:",dealerValue,"\n")

    #Player draw:
    playerHand.addCard(deck.draw())
    playerHand.addCard(deck.draw())
    playerValue = playerHand.getValue()
    print("YOUR HAND\n"+playerHand.displayCards())
    print("Value of Your Hand:",playerValue,"\n")
    
    #Player given options 'Hit' or 'Stand'
    while playerValue < 21:
        i = input("Hit or Stand?\n")
        #if Hit player recieves another card and value is updated
        if i.lower() == "hit":
            playerHand.addCard(deck.draw())
            playerValue = playerHand.getValue()
            print("\nYOUR HAND\n"+playerHand.displayCards())
            print("Value of Hand:",playerValue,"\n")
        elif i.lower() == "stand":
            break


    #dealer turn
    if playerValue <= 21:
        while dealerValue < playerValue:
            dealerHand.addCard(deck.draw())
            dealerValue = dealerHand.getValue()
            print("\nDEALERS HAND\n"+dealerHand.displayCards())
            print("Value of dealer hand:",dealerValue,"\n")
        if playerValue > dealerValue or dealerValue > 21:
            print("\nWIN")
        elif playerValue == dealerValue:
            print("\nDRAW")
        elif dealerValue > playerValue:
            print("\nLOSE")
    else:
        print("\nBUST")



if __name__ == '__main__':
    play()
