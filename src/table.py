class Table:
    def __init__(self,player_chips,bet_amount):
        self.player_chips = player_chips
        self.bet_amount = bet_amount

    def update(self,player_hand,dealer_hand):
        print("Dealer's hand:  ", end = '')
        for card in dealer_hand.cards:
            print(f'{card.rank}{card.suit}   ', end = '')
        print('\n')
        print("Player's hand:  ", end = '')
        for card in player_hand.cards:
            print(f'{card.rank}{card.suit}   ', end = '')
        print('\n')
        print(f'Bet amount: £{self.bet_amount}')
        print(f'Chips available: £{self.player_chips}')

