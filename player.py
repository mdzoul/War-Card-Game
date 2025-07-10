"""
Code to keep track of all cards in player's hand;
And the ability to add or remove cards from said hand
"""


class Player:
    """This class will be used to hold a player's current list of cards"""

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_card(self):
        """A player should be able to remove card from list of Card objects"""
        return self.all_cards.pop(0)

    def add_card(self, new_cards):
        """Allow players to add a single or multiple cards to their list"""
        if isinstance(new_cards, list):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single Card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
