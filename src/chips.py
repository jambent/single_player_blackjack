from src.hand import Hand

class Chips:
    "Amount of money available to player"

    def __init__(self, cash):
        self.available = cash

    def __repr__(self):
        return f'Chips({self.available})'

    def place_bet(self, bet_amount):
        bet_amount_as_number = float(bet_amount)
        if self.available - bet_amount_as_number >= 0:
            self.available -= bet_amount_as_number

    def add_winnings(self,bet_amount,blackjack):
        bet_amount_as_number = float(bet_amount)
        if blackjack == True:
            self.available += 2.5 * bet_amount_as_number
        else:
            self.available += 2 * bet_amount_as_number 

    def return_bet(self,bet_amount):
        bet_amount_as_number = float(bet_amount)
        self.available += bet_amount_as_number
