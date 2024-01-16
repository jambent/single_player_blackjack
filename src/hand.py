from itertools import combinations_with_replacement

class Hand:
    "Cards that player or dealer holds"
    def __init__(self,*cards):
        value = 0
        number_of_aces = 0
        for card in cards:
            card_rank = card.rank
            if card_rank in ['J','Q','K']:
                value += 10
            elif card_rank == 'A':
                number_of_aces += 1
            else:
                value += int(card_rank)
        
        if number_of_aces > 0:
            ace_possibilities = combinations_with_replacement([1,11],number_of_aces)


        self.value = value
