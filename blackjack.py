from src.deck import Deck
from src.card import Card
from src.hand import Hand
from src.player import Player
from src.dealer import Dealer

def play():
    playing = True
    round = 1
    print("Welcome To Blackjack!")
    print("Your objective is to get as close to 21 as you can without going over.")
    print("Your balance starts at 100 per player.")
    print("Good Luck!\n")

    dealer = Dealer("DEALER")

    #Gets players to select the rules they want to play with
    ruleOneSet = False
    ruleTwoSet = False
    ruleFor17 = True
    print("Please set the rules for your table:")
    while ruleOneSet == False:
        try:
            rule = input("Should the dealer hit or stand when dealt a soft 17? (h/s)\n")
            if rule.lower() == "hit" or rule.lower() == "h":
                ruleFor17 = True
                ruleOneSet = True
            elif rule.lower() == "stand" or rule.lower() == "s":
                ruleFor17 = False
                ruleOneSet = True
            else:
                print("Please enter \"h\" or \"s\"")
        except:
            print("Invalid input, please try again.")
    while ruleTwoSet == False:
        try:
            rule = input("Should the player win if they are dealt 5 cards without going bust? (y/n)\n")
            if rule.lower() == "yes" or rule.lower() == "y":
                fiveCardWin = True
                ruleTwoSet = True
            elif rule.lower() == "no" or rule.lower() == "n":
                fiveCardWin = False
                ruleTwoSet = True
            else:
                print("Please enter \"y\" or \"n\"")
        except:
            print("Invalid input, please try again.")

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
            name = str(input("Please input player {}'s name: ".format(p)))
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
            #Player sets wager
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
            #if player has 5 cards and is not bust, they win
            while p.getValue() < 21:
                i = input("Hit or Stand? h/s\n")
                #If Hit player recieves another card and value is updated
                if i.lower() == "hit" or i.lower() == "h":
                    p.hit(deck)
                    display(p)
                elif i.lower() == "stand" or i.lower() == "s":
                    break
                else:
                    print("Please enter \"h\" or \"s\"")
            
            if p.getValue() > 21:
                print("BUST\n")
            #If players hand contains 5 cards without going over 21, they win
            elif p.getHand().amountCards() == 5 and fiveCardWin == True:
                p.setFiveCards()
                print("FIVE CARD WIN")
        
        #Dealer turn
        display(dealer)
        
        #dealer plays hand
        if bool(players):
            dealer.playHand(deck, ruleFor17)

        #Check players outcome
        pRem = []
        for p in players:
            print("{}: {}".format(str(p.getName()), str(dealer.evaluate(p))))
            print("Your balance is now: {}".format(p.getMoney()))
        
            if p.getMoney() == 0:
                pRem.append(p)
                print("Game Over")
                if len(players) == 1:
                    playing = False
            else:
                p.clearHand()
        
        #Removes any players with no remaining money
        for i in pRem:
            try:
                players.remove(i)
            except:
                pass

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
                    elif playAgain.lower() == "n":
                        playing = False
                        noinput = False
                    else:
                        print("Please enter \"y\" or \"n\".")
                except:
                    print("Invalid input, please input \"y\" or \"n\"")

#Displays a players hand (inc dealer)
def display(p):
    print("{}'s HAND\n{}".format(p.getName(), p.getHand().displayCards()))
    print("Value of Hand: {}\n".format(p.getValue()))

if __name__ == '__main__':
    play()