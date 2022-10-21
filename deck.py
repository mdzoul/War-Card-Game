"""Code for creating a full deck of cards in a list, shuffling them, and dealing cards"""
from random import shuffle
from card import Card, SUITS, RANKS


class Deck:
    """Instantiate a new deck"""
    def __init__(self):
        self.all_cards = []
        # Create all 52 Card objects
        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        """Shuffle a Deck through a method call"""
        shuffle(self.all_cards)

    def deal_card(self):
        """Deal cards from the Deck object"""
        return self.all_cards.pop()
