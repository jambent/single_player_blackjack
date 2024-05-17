# Single-player Blackjack
A CLI implementation of Blackjack for a single player versus a computer dealer, using a single deck of cards


## Installation
#### Create virtual environment, and activate:
```
python -m venv venv

source venv/bin/activate
```

#### Install required packages from requirements.txt file:
```
pip install -r requirements.txt
```

## Run the program
```
PYTHONPATH=$(pwd)/ python src/main.py
```
## In play
You start with £100 in chips:
```
Chips available: £100

Place your bet by typing in number (e.g., 1 == £1.00): 
```
After placing your bet, the Dealer's and Player's hand are presented, along with a record of the bet amount and your remaining chips value not in play, e.g.,
```
Dealer's hand:  JS   

Player's hand:  KD   8C   

Bet amount: £2
Chips available: £98.0

Hit or Stand? (type 'h' or 's')
```
A card consists of 2 values: the rank and the suit.  
Possible ranks are 2 3 4 5 6 7 8 9 10 J Q K or A, where J, Q, K and A represent Jack, Queen, King and Ace, respectively.
Jack, Queen, King and Ace have a value of 10, but an Ace can take a value of either 1 or 11.
Possible suits are H D C S, representing Hearts, Diamonds, Clubs and Spades.
In the above example, the Dealer holds the Jack of Spades (JS) and the Player holds the King of Diamonds and the 8 of Clubs (KD and 8C).

In the event that your two-card, initial hand has a value of 21 (an Ace plus a 10, Jack, Queen, or King), the Dealer immediately draws one card.
If the value of the two-card Dealer's hand is also 21, your bet is returned.  However if the value of the Dealer's hand is less than 21, you win 2.5 times the value of your bet.

If your two-card hand does not have a value of 21, you are presented with the opportunity to Hit (take another card) or Stand (keep your hand as it is), until you decide to Stand or you go bust.
You go bust if the value of your hand exceeds 21.  In this case the Dealer wins and you lose your bet.

Once you Stand, the Dealer must draw cards until the value of his hand is at least 17, or he goes bust by creating a hand that has a value greater than 21.  If the Dealer goes bust you win 2 times the value of your bet.


If the Dealer finishes drawing cards and has not gone bust, the value of the Dealer's and Player's hands are compared.  If the values of the hands are identical, your bet is returned.  If the Dealer's hand has a greater value, you lose your bet.  If the Player's hand has a greater value, you win 2 times the value of your bet. 

Regardless of who wins, or if it's a tie, you are presented with the opportunity to play another round:
```
Would you like to play another round? (y/n)
```
If you type 'n', your remaining chips value is displayed, and the program exits to the terminal command prompt.

### Notes
Due to an incompatibility between Python 3.12 and autopep8, Python 3.11 was deliberately selected for use instead
