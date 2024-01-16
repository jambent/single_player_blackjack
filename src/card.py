class Card:
    "One standard playing card"

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f'Card({self.rank},{self.suit})'
