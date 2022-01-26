import pygame
import deck
import stages
import player
import blocks
import cards


class Game:
    types_players = {'user': player.User, 'bot': player.Bot}

    def __init__(self):
        """params pygame"""
        self.size = self.width, self.height = 800, 500
        self.window = blocks.Window()
        self.window.size = self.size
        self.screen = pygame.display.set_mode(self.size)
        self.running = True
        self.all_sprites = pygame.sprite.Group()

        """params first game"""
        self.board = blocks.Board((0, 0), (0.83, 1), self.window)
        self.deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
        self.players = ['user.You.0', 'bot.Vlad.1', 'bot.Alina.2']
        self.start_player_id = 0
        self.count_players = 3
        self.sgs = stages.Stages(self)
        self.stage = 'start'
        self.protected_players = []

        """init elements"""
        self.init_players()
        self.init_deck()
        self.card = cards.Card2(self.all_sprites, self.deck)
        self.sgs.start_game()

    def game_cycle(self):
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.sgs.execute_stage_by_name(self.stage, event)
            self.screen.fill(pygame.Color((113, 130, 255)))
            self.render()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
        pygame.quit()

    def init_deck(self):
        dk = deck.Deck(self.board)
        dk.fill_and_shuffle_deck(self.deck, self.all_sprites)
        self.deck = dk

    def init_players(self):
        ps = []
        for p in self.players:
            type_player, name, slot = p.split('.')
            ps.append(self.types_players[type_player](self, self.board, name, slot))
        self.players = ps

    def render(self):
        self.board.render(self.screen)
        [p.render(self.screen) for p in self.players]

    def give_card(self, p):
        card = self.deck.get_and_pop_card()
        if type(p) == player.User:
            card.reverse_self()
        p.take_card(card)

    def next_turn(self):
        self.start_player_id += 1
        self.start_player_id %= self.count_players

    def now_player(self):
        return self.players[self.start_player_id]

    def kill_player(self, p):
        del self.players[self.players.index(p)]
        self.count_players -= 1
        if self.start_player_id == self.count_players:
            self.start_player_id -= 1


game = Game()
game.game_cycle()
