import random

from src.card import Card


class Deck:
    "Standard 52-card deck"

    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
        suits = ['C', 'D', 'H', 'S']

        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(rank, suit))
        self.deck = deck

    def shuffle(self):
        "Shuffles cards in deck"
        return random.shuffle(self.deck)

    def deal_one_card(self):
        "Removes one card from end of deck"
        return self.deck.pop()
