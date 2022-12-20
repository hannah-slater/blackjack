from src.deck import Deck
from src.card import Card
from src.hand import Hand
from src.player import Player

def play():
    playing = True
    round = 1
    print("Welcome To Blackjack!")
    print("Your objective is to get as close to 21 as you can without going over.")
    print("Your balance starts at 100 per player.")
    print("Good Luck!\n")

    dealer = Player("DEALER")

    playerAmnt = 0
    #Allows players to initiate up to 5 players
    while playerAmnt not in range(1,6):
        try:
            playerAmnt = int(input("Please enter the number of players (up to 5): "))
            if playerAmnt not in range(1,6):
                print("Invalid input, please enter a number between 1 and 5.")

        except:
            print("Invalid input, please enter a number between 1 and 5.")

    players = []
    for p in range(1, playerAmnt + 1):
        try:
            name = str(input("Please input players name: "))
            players.append(Player(name.upper()))
        except:
            print("Invalid input, please input a name.")

    while(playing):
        print("\nROUND",round)

        deck = Deck()
        deck.shuffle()

        dealer.clearHand()
        dealer.createHand(deck)

        for p in players:
            setWager = False
            while setWager is False:
                try:
                    wager = int(input("{} how much would you like to wager?\n".format(p.getName())))
                    if wager <= p.getMoney():
                        p.setWager(wager)
                        setWager = True
                    else:
                        print("Wager is invalid, your balance: {}".format(p.getMoney()))
                except:
                    print("Invalid input, please input an integer number.")

            p.createHand(deck)
            display(p)
        
            #Player given options 'Hit' or 'Stand'
            while p.getValue() < 21:
                i = input("Hit or Stand? h/s\n")
                #If Hit player recieves another card and value is updated
                if i.lower() == "hit" or i.lower() == "h":
                    p.hit(deck)
                    display(p)
                elif i.lower() == "stand" or i.lower() == "s":
                    break
            if p.getValue() > 21:
                print("BUST\n")
        
        #Dealer turn
        display(dealer)
        
        if bool(players):
            while dealer.getValue() < 17:
                dealer.hit(deck)
                display(dealer)

        #Check players outcome
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
                
            print("Your balance is now: {}".format(p.getMoney()))
        
            if p.getMoney() == 0:
                pCopy.append(0)
                print("Game Over")
                if len(players) == 1:
                    playing = False
            else:
                pCopy.append(1)
                p.clearHand()
        
        #Removes any players with no remaining money
        a = 0
        for i in pCopy:
            b = 0
            for p in players:
                b = p
            if i == 0:
                players.remove(b)
            a += 1

        if len(players) == 0:
            print("All players out")
            playing = False
        
        if playing:
            noinput = True
            while noinput:
                try:
                    playAgain = input("\nPlay again? y/n\n")
                    if playAgain.lower() == "y":
                        round += 1
                        noinput = False
                    else:
                        playing = False
                        noinput = False
                except:
                    print("Invalid input, please input \"y\" or \"n\"")

#Displays a players hand (inc dealer)
def display(p):
    print("{}'s HAND\n{}".format(p.getName(), p.getHand().displayCards()))
    print("Value of Hand: {}\n".format(p.getValue()))

if __name__ == '__main__':
    play()