# Blackjack
Blackjack game for BBC Technical Test 2022/23
Implemented as a command line game

## Running the game
Type **'python3 blackjack.py'** in the command line

Python version 3.9.7

## Running unit test
Type **'python3 -m unittest discover test'** in command line

## Assumptions made
- The house would not hit their own hand if they are winning once players have played through
- A player cannot wager more money then they have available
- If a player runs out of money they are removed from the game
- A player will win the same amount they wagered, plus getting their wager back
- If a player draws with the dealer, their wager will be returned
- If the dealer's hand is below 17 they must hit until it isn't
- A player can only hit or stand when their card total is less than 21
- If a player is dealt or hits to reach exactly 21, they would not be offered to hit or stand as they have blackjack
- A player wins if they beat the dealer, the other players hands are inconsequential to whether or not that player wins