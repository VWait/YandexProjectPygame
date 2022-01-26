import math


class Player:
    def __init__(self, game, board, name, number_place):
        self.game = game
        self.name = name
        self.board = board
        self.cards = [None, None]
        self.hand = self.board.get_hand_by_number(number_place)
        self.clicked = 0
        self.cards_left = []

        self.selected_card = 0
        self.target = 0
        self.selected_number = 0

    def get_index_other_card(self, card):
        return (self.cards.index(card) + 1) % 2

    def render(self, screen):
        self.hand.render(screen, self.name)
        self.hand.cards_played(screen, self.cards_left)
        [card.render(screen) for card in self.cards if card]

    def take_card(self, card):
        self.cards[0], self.cards[1] = card, self.cards[0]
        self.cards[0].change_pos0(self.hand.get_pos0_card(0))
        self.cards[0].parent = self
        if self.cards[1]:
            self.cards[1].change_pos0(self.hand.get_pos0_card(1))

    def click_card(self, pos):
        for card in self.cards:
            if card:
                if card.rect.collidepoint(pos):
                    card.click()

    def click_hand(self, pos):
        if self.hand.rect.collidepoint(pos) and self not in self.game.protected_players:
            if self.hand.clicked == 0:
                for p in self.game.players:
                    p.hand.clicked = 0
                self.hand.clicked += 1
            else:
                self.hand.clicked = 0
                self.game.now_player().target = self
                self.game.stage = 'next_turn'

    def click_number(self, pos):
        for n, i in enumerate(self.hand.circles):
            if math.sqrt((i[0] - pos[0]) ** 2 + (i[1] - pos[1]) ** 2) <= self.hand.radius:
                if self.hand.now_circle[0] == n + 1:
                    self.hand.now_circle = (0, 0)
                    self.selected_number = n + 1
                    self.game.stage = 'next_turn'
                else:
                    self.hand.now_circle = (n + 1, i)

    def pre_move(self, card):
        self.selected_card = card
        self.game.stage = card.next_stage

    def play_and_discard_card(self):
        self.cards_left.append(self.selected_card.value)
        self.selected_card.effect(self, self.selected_card, self.target, self.selected_number)
        del self.cards[self.cards.index(self.selected_card)]
        self.selected_card.kill()
        self.cards.append(None)
        self.game.stage = 'next_turn'

    def kill_self(self):
        self.game.kill_player(self)
        for card in self.cards:
            if card:
                card.kill()


class Bot(Player):
    def click_card(self, pos):
        self.selected_card = 0
        for card in self.cards:
            if card.value == 8:
                self.selected_card = self.cards[self.get_index_other_card(card)]
            elif card.value == 7:
                self.selected_card = card
        if not self.selected_card:
            self.selected_card = self.cards[0]

        self.target = self.game.players[(self.game.start_player_id + 1) % self.game.count_players]
        self.selected_number = 5

        self.game.stage = 'next_turn'


class User(Player):
    pass
