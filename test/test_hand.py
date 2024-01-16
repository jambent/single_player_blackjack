from src.hand import Hand
from src.card import Card


def test_that_hand_values_without_aces_calculated_correctly():
    card1 = Card(4, 'H')
    card2 = Card(3, 'S')
    card3 = Card('Q', 'D')
    card4 = Card('J', 'C')

    hand1 = Hand(card1, card2)
    hand2 = Hand(card1, card3)
    hand3 = Hand(card3, card4)
    hand4 = Hand(card1, card2, card4)

    assert hand1.value() == 7
    assert hand2.value() == 14
    assert hand3.value() == 20
    assert hand4.value() == 17


def test_that_hand_values_with_aces_calculated_correctly():
    card1 = Card('A', 'S')
    card2 = Card('A', 'H')
    card3 = Card('K', 'D')
    card4 = Card('9', 'C')

    hand1 = Hand(card1, card2)
    hand2 = Hand(card1, card2, card3)
    hand3 = Hand(card1, card3)
    hand4 = Hand(card2, card3, card4)
    hand5 = Hand(card1, card4)

    assert hand1.value() == 12
    assert hand2.value() == 12
    assert hand3.value() == 21
    assert hand4.value() == 20
    assert hand5.value() == 20
