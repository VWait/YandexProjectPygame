import pygame


class Stages:
    def __init__(self, gm):
        self.game = gm
        self.names_stages = {'start': self.start_game, 'choice_card': self.choice_card,
                             'end': self.end_game, 'choice_player': self.choice_player,
                             'next_turn': self.next_turn, 'choice_number': self.choice_number}

    def start_game(self):
        [self.game.give_card(p) for p in self.game.players]
        self.game.give_card(self.game.players[self.game.start_player_id])
        self.game.stage = 'choice_card'

    def choice_card(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.now_player().click_card(event.pos)

    def choice_number(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.now_player().click_number(event.pos)

    def choice_player(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            [p.click_hand(event.pos) for p in self.game.players]

    def card_effect(self, event):
        self.game.now_player().play_and_discard_card()

    def next_turn(self, event):
        if self.game.now_player().selected_card.value == 1 and self.game.now_player().selected_number == 0:
            self.game.stage = 'choice_number'
        else:
            self.game.now_player().play_and_discard_card()
            self.game.next_turn()
            self.game.stage = 'choice_card'
            self.game.give_card(self.game.now_player())
            if self.game.now_player() in self.game.protected_players:
                del self.game.protected_players[self.game.protected_players.index(self.game.now_player())]
        if self.game.count_players == 1 or len(self.game.deck.cards) == 1:
            self.game.stage = 'end'

    def end_game(self, event):
        pass

    def execute_stage_by_name(self, name, event):
        self.names_stages[name](event)
