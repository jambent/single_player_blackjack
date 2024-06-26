from src.deck import Deck
from src.chips import Chips
from src.hand import Hand
from src.table import Table


if __name__ == '__main__':

    player_chips = Chips(100)

    another_round = 'y'
    while another_round != 'n':

        cards = Deck()
        cards.shuffle()

        bet_amount = player_chips.available + 1
        while player_chips.available - float(bet_amount) < 0:
            print(f'Chips available: £{player_chips.available}\n')
            bet_amount = input(
                'Place your bet by typing in number (e.g., 1 == £1.00): ')
            if player_chips.available - float(bet_amount) >= 0:
                break
            print('You have insufficient funds')

        player_chips.place_bet(bet_amount)

        player_card_one = cards.deal_one_card()
        dealer_card_one = cards.deal_one_card()
        player_card_two = cards.deal_one_card()

        player_hand = Hand(player_card_one, player_card_two)
        player_hand_value = player_hand.value()

        dealer_hand = Hand(dealer_card_one)

        table = Table(player_chips.available, bet_amount)
        table.update(player_hand, dealer_hand)

        if player_hand_value == 21:

            dealer_card_two = cards.deal_one_card()
            dealer_hand.add_to_hand(dealer_card_two)
            table.update(player_hand, dealer_hand)

            if dealer_hand.value() != 21:
                player_chips.add_winnings(bet_amount, True)
                print('\nYou win')
                print(f'Chips available: £{player_chips.available}\n')
            else:
                player_chips.return_bet(bet_amount)
                print("\nIt's a tie")
                print(f'Chips available: £{player_chips.available}\n')

        else:

            player_instruction = ''
            while player_instruction != 's':
                player_instruction = input("\nHit or Stand? (type 'h' or 's')")
                if player_instruction == 'h':
                    new_player_card = cards.deal_one_card()
                    player_hand.add_to_hand(new_player_card)
                    table.update(player_hand, dealer_hand)
                    if player_hand.value() > 21:
                        break
   
            if player_hand.value() < 22:
                dealer_card_two = cards.deal_one_card()
                dealer_hand.add_to_hand(dealer_card_two)
                table.update(player_hand, dealer_hand)
                while dealer_hand.value() < 17:
                    new_dealer_card = cards.deal_one_card()
                    dealer_hand.add_to_hand(new_dealer_card)
                    table.update(player_hand, dealer_hand)

            player_hand_value = player_hand.value()
            dealer_hand_value = dealer_hand.value()
            if dealer_hand_value <= 21 and player_hand_value > 21:
                print('\nDealer wins')
                print(f'Chips available: £{player_chips.available}\n')
            elif dealer_hand_value > 21 and player_hand_value <= 21:
                player_chips.add_winnings(bet_amount, False)
                print('\nYou win')
                print(f'Chips available: £{player_chips.available}\n')
            elif (player_hand_value > dealer_hand_value
                and player_hand_value <= 21):
                player_chips.add_winnings(bet_amount, False)
                print('\nYou win')
                print(f'Chips available: £{player_chips.available}\n')
            elif dealer_hand_value > 21 and player_hand_value > 21:
                print('\nDealer wins')
                print(f'Chips available: £{player_chips.available}\n')
            elif (dealer_hand_value > player_hand_value
                and dealer_hand_value <= 21):
                print('\nDealer wins')
                print(f'Chips available: £{player_chips.available}\n')
            elif (dealer_hand_value == player_hand_value
                and player_hand_value <= 21):
                player_chips.return_bet(bet_amount)
                print("\nIt's a tie")
                print(f'Chips available: £{player_chips.available}\n')

        another_round = input('Would you like to play another round? (y/n)\n')

    print(f'\nYou leave the table with £{player_chips.available}')
