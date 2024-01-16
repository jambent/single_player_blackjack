from itertools import combinations_with_replacement


class Hand:
    "Cards that player or dealer holds"

    def __init__(self, *cards):
        self.cards = [card for card in cards]

    def value(self):
        hand_value = 0
        number_of_aces = 0
        for card in self.cards:
            card_rank = card.rank
            if card_rank in ['J', 'Q', 'K']:
                hand_value += 10
            elif card_rank == 'A':
                number_of_aces += 1
            else:
                hand_value += int(card_rank)

        final_hand_value_possibilities = []

        if number_of_aces > 0:
            ace_values_possibilities = \
                combinations_with_replacement([1, 11], number_of_aces)
            for possibility in ace_values_possibilities:
                possible_final_hand_value = hand_value
                for ace_value in possibility:
                    possible_final_hand_value += ace_value
                if possible_final_hand_value <= 21:
                    final_hand_value_possibilities.append(
                        possible_final_hand_value)
            return max(final_hand_value_possibilities)
        else:
            return hand_value
