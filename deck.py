from cards import Card1, Card2, Card3, Card4, Card5, Card6, Card7, Card8
from random import shuffle


class Deck:
    values_cards = {1: Card1, 2: Card2, 3: Card3, 4: Card4,
                    5: Card5, 6: Card6, 7: Card7, 8: Card8}

    def __init__(self, board):
        self.cards = []
        self.board = board

    def save_card(self, value, group):
        self.cards.append(self.values_cards[value](group, self))

    def fill_and_shuffle_deck(self, dk_vals, group):
        [self.save_card(value, group) for value in dk_vals]
        shuffle(self.cards)

    def get_and_pop_card(self):
        return self.cards.pop(0)

    def get_pos0_card(self):
        return 700, 200
