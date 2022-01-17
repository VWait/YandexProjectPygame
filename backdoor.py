from random import shuffle


class Card:
    def move(self):
        pass


class Card1(Card):
    pass


class Card2(Card):
    pass


class Card3(Card):
    pass


class Card4(Card):
    pass


class Card5(Card):
    pass


class Card6(Card):
    pass


class Card7(Card):
    pass


class Card8(Card):
    pass


values_cards = {1: Card1, 2: Card2, 3: Card3, 4: Card4,
                5: Card5, 6: Card6, 7: Card7, 8: Card8}


class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.deck = []
        self.fill_and_shuffle_deck()

    def save_card(self, value):
        self.deck.append(values_cards[value])

    def fill_and_shuffle_deck(self):
        [self.save_card(value) for value in self.cards]
        shuffle(self.deck)

    def get_and_pop_card(self):
        return self.deck.pop(0)


class Player:
    def __init__(self, start_card):
        self.card = start_card

    def move(self, dk):
        self.card = [self.card, dk.get_and_pop_card()] # player take one more card
        self.choice_of_card()

    def choice_of_card(self):
        choice = int(input('0 или 1'))
        self.card[choice].move() # discard one card
        self.card = self.card[(choice + 1) % 2] # save other card


deck = Deck([1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8])
count_players = 3
players = [Player(deck.get_and_pop_card()) for i in range(count_players)]
player_i = 0


while True:
    break
