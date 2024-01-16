from src.deck import Deck
from src.chips import Chips
from src.hand import Hand

if __name__ == '__main__':
    cards = Deck()
    cards.shuffle()

    player_chips = Chips(100)

    bet_amount = player_chips.available + 1
    while player_chips.available - float(bet_amount) < 0:
        print(f'Chips available: £{player_chips.available}\n')
        bet_amount = input(
            'Place your bet by typing in number (e.g., 1 == £1.00):\n')
        if player_chips.available - float(bet_amount) >= 0:
            break
        print('You have insufficient funds')

    player_chips.place_bet(bet_amount)

    player_card_one = cards.deal_one_card()
    dealer_card = cards.deal_one_card()
    player_card_two = cards.deal_one_card()

    player_hand = Hand(player_card_one, player_card_two)
