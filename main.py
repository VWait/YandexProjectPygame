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
        self.label = 'Начать игру'
        self.font = pygame.font.SysFont('arial', 50)
        self.color = (113, 130, 255)

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.players[0].click_blip(event.pos)
                    self.players[0].click_begin(event.pos)
                self.sgs.execute_stage_by_name(self.stage, event)
                self.board.hint_step = self.stage
            self.screen.fill(pygame.Color(self.color))
            pygame.draw.circle(self.screen, (255, 255, 255),
                               (self.size[0] / 2, self.size[1] * 0.4), self.board.radius * 5, width=5)
            pygame.draw.polygon(self.screen, (255, 255, 255), [[self.size[0] / 1.9, self.size[1] / 3],
                                [self.size[0] / 2.2, self.size[1] * 0.4],
                                [self.size[0] / 1.9, self.size[1] / 2.15]])
            text = self.font.render(self.label, True, (255, 255, 255))
            self.screen.blit(text, (self.size[0] * 0.35, self.size[1] * 0.6))
            self.render()
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
        if self.stage == 'end':
            return
        self.board.render(self.screen)
        [p.render(self.screen) for p in self.players]
        self.all_sprites.draw(self.screen)

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

    def repeat(self):
        self.__init__()


game = Game()
game.game_cycle()
