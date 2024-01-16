class Chips:
    "Amount of money available to player"
    def __init__(self,cash):
        self.available = cash

    def place_bet(self,bet_amount):
        bet_amount_as_number = float(bet_amount)
        if self.available - bet_amount_as_number >= 0:
            self.available -= bet_amount_as_number