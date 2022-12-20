from src.deck import Deck
from src.card import Card
from src.hand import Hand
from src.player import Player

def play():
    playing = True
    print("Welcome To Blackjack!\n")
    print("Your objective is to get as close to 21 as you can without going over.\n")
    print("Good Luck!\n")

    dealer = Player("DEALER")

    playerAmnt = 0
    #loops until user inputs a valid number
    while playerAmnt not in range(1,6):
        playerAmnt = int(input("Please enter the number of players (up to 5): "))
        if playerAmnt not in range(1,6):
            print("Invalid input, please try again.")

    players = []
    for p in range(1, playerAmnt + 1):
        name = str(input("Please input players name: "))
        players.append(Player(name.upper()))

    while(playing):
        deck = Deck()
        deck.shuffle()

        #Dealer draw:
        dealer.clearHand()
        dealer.createHand(deck)

        #Player draw:
        for p in players:
            setWager = False
            while setWager is False:
                wager = int(input("{} how much would you like to wager?\n".format(p.getName())))
                if wager <= p.getMoney():
                    p.setWager(wager)
                    setWager = True
                else:
                    print("Wager is invalid, your balance: "+str(p.getMoney()))
            
            p.createHand(deck)
            print(str(p.getName())+"'s HAND\n"+str(p.getHand().displayCards()))
            print("Value of Hand:",p.getValue(),"\n")
        
            #Player given options 'Hit' or 'Stand'
            while p.getValue() < 21:
                i = input("Hit or Stand?\n")
                #if Hit player recieves another card and value is updated
                if i.lower() == "hit" or i.lower() == "h":
                    p.hit(deck)
                    print("\n"+str(p.getName())+"'s HAND\n"+str(p.getHand().displayCards()))
                    print("Value of Hand:",p.getValue(),"\n")
                elif i.lower() == "stand" or i.lower() == "s":
                    break
            if p.getValue() > 21:
                print("BUST\n")
        
        #dealer turn
        print("DEALERS HAND\n"+dealer.getHand().displayCards())
        print("Value of dealer's hand:",dealer.getValue(),"\n")
        if bool(players):
            while dealer.getValue() < 17:
                dealer.hit(deck)
                print("\nDEALERS HAND\n"+dealer.getHand().displayCards())
                print("Value of dealer hand:",dealer.getValue(),"\n")

        #check if players won, drew or lost
        dVal = dealer.getValue()
        pCopy = []
        for p in players:
            pVal = p.getValue()
            pName = p.getName()
            if pVal > 21:
                print(pName+": BUST")
            elif dVal > 21:
                print(pName+": WIN")
                p.addWinnings()
            elif pVal > dVal:
                print(pName+": WIN")
                p.addWinnings()
            elif pVal == dVal:
                print(pName+": DRAW")
                p.draw()
            elif pVal < dVal:
                print(pName+": LOSE")
                
            print("Your balance is now: "+str(p.getMoney()))
        
            if p.getMoney() == 0:
                pCopy.append(0)
                print("Game Over")
            else:
                pCopy.append(1)
                p.clearHand()
        
        a = 0
        for i in pCopy:
            if i == 0:
                players.pop(a)
            a += 1

                
        if players is False:
            print("All players out")
            playing = False
        
        playAgain = input("Play again? y/n\n")
        if playAgain.lower() == "n":
            playing = False

if __name__ == '__main__':
    play()