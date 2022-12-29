# Blackjack
Blackjack game for BBC Technical Test 2022/23
Implemented as a command line game

## Running the game
Type **'python3 blackjack.py'** in the command line

Python version 3.9.7

## Assumptions made
- The house would not hit their own hand if they are winning once players have played through
- A player cannot go into debt by wagering more money then they have available
- If a player runs out of money they are removed from the game
- If a player wins they make what they wagered, plus getting their wager back
- If a player draws they just get their wager returned
- A player can only hit or stand when their card total is less than 21
- If a player is dealt or hits to reach exactly 21, they would not be offered to hit or stand as hitting would ruin their blackjack
- A player wins if they beat the dealer, the other players hands are inconsequential to whether or not that player wins