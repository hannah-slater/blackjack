from src.deck import Deck
from src.card import Card
from src.hand import Hand
from src.player import Player

def play():
    deck = Deck()
    deck.shuffle()

    print("Welcome To Blackjack!\nYour objective is to get as close to 21 as you can without going over.\nGood Luck!\n")

    playerAmnt = 0
    #loops until user inputs a valid number
    while playerAmnt not in range(1,6):
        playerAmnt = int(input("Please enter the number of players (up to 5): "))
        if playerAmnt not in range(1,6):
            print("Invalid input, please try again.")
    
    players = []
    for p in range(1, playerAmnt + 1):
        name = str(input("Please input player's name: "))
        players.append(Player(name.upper()))
         
    #Dealer draw:
    dealer = Player("DEALER")
    dealer.createHand(deck)
    print("DEALERS HAND\n"+dealer.getHand().displayCards())
    print("Value of dealer's hand:",dealer.getValue(),"\n")

    #Player draw:
    for p in players:
        p.createHand(deck)
        print(p.getName()+"'s HAND\n"+p.getHand().displayCards())
        print("Value of Hand:",p.getValue(),"\n")
    
        #Player given options 'Hit' or 'Stand'
        while p.getValue() < 21:
            i = input("Hit or Stand?\n")
            #if Hit player recieves another card and value is updated
            if i.lower() == "hit":
                p.hit(deck)
                print("\n"+p.getName()+"'s HAND\n"+p.getHand().displayCards())
                print("Value of Hand:",p.getValue(),"\n")
            elif i.lower() == "stand":
                break
        if p.getValue() > 21:
            print("BUST\n")

    #dealer turn
    if bool(players):
        while dealer.getValue() < 17:
            dealer.hit(deck)
            print("\nDEALERS HAND\n"+dealer.getHand().displayCards())
            print("Value of dealer hand:",dealer.getValue(),"\n")

    dVal = dealer.getValue()
    for p in players:
        pVal = p.getValue()
        pName = p.getName()
        if pVal > 21:
            print(pName+": BUST\n")
        elif dVal > 21:
            print(pName+": WIN\n")
        elif pVal > dVal:
            print(pName+": WIN\n")
        elif pVal == dVal:
            print(pName+": DRAW\n")
        elif pVal < dVal:
            print(pName+": LOSE\n")
                

if __name__ == '__main__':
    play()
