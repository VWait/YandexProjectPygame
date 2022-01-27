import pygame
import os
from player import Bot


class Card(pygame.sprite.Sprite):
    def load_image(self, name, color_key=None):
        fullname = os.path.join('data', name)
        try:
            image = pygame.image.load(fullname).convert()
        except pygame.error as message:
            print('Cannot load image:', name)
            raise SystemExit(message)

        if color_key is not None:
            if color_key == -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
        return image

    def __init__(self, group, value, parent):
        super().__init__(group)
        self.images = [self.load_image('back-card.png'), self.load_image(f'card{value}.png')]
        self.now_image = 0
        self.image = self.images[self.now_image]
        self.value = value
        self.parent = parent
        self.size = (70, 100)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = parent.get_pos0_card()
        self.clicked = 0

    def change_pos0(self, pos0):
        self.rect.x, self.rect.y = pos0

    def reverse_self(self):
        self.now_image += 1
        self.now_image %= 2
        self.image = self.images[self.now_image]

    def click(self):
        if self.clicked == 0:
            for card in self.parent.cards:
                card.clicked = 0
        self.clicked = (self.clicked + 1) % 2
        if self.clicked == 0:
            self.parent.pre_move(self)

    def contour_card(self, screen):
        block_pos0 = self.rect.x - 3, self.rect.y - 3
        block_size_window = self.size[0] + 6, self.size[1] + 6
        pygame.draw.rect(screen, (255, 255, 255), block_pos0 + block_size_window, 3)

    def render(self, screen):
        if self.clicked == 1:
            self.contour_card(screen)

    def effect(self, player, card, target, number):
        pass


class Card1(Card):
    def __init__(self, group, parent):
        super().__init__(group, 1, parent)
        self.next_stage = 'choice_player'

    def effect(self, player, card, target, number):
        if target.cards[0].value == number:
            target.kill_self()


class Card2(Card):
    def __init__(self, group, parent):
        super().__init__(group, 2, parent)
        self.next_stage = 'choice_player'

    def effect(self, player, card, target, number):
        if player != target:
            if type(target) == Bot:
                target.cards[0].reverse_self()


class Card3(Card):
    def __init__(self, group, parent):
        super().__init__(group, 3, parent)
        self.next_stage = 'choice_player'

    def effect(self, player, card, target, number):
        if card.value > target.cards[0].value:
            target.kill_self()
        elif card.value < target.cards[0].value:
            player.kill_self()


class Card4(Card):
    def __init__(self, group, parent):
        super().__init__(group, 4, parent)
        self.next_stage = 'next_turn'

    def effect(self, player, card, target, number):
        self.parent.game.protected_players.append(player)


class Card5(Card):
    def __init__(self, group, parent):
        super().__init__(group, 5, parent)
        self.next_stage = 'choice_player'

    def effect(self, player, card, target, number):
        if player != target:
            target.cards[0].kill()
            target.cards[0] = None
            self.parent.game.give_card(target)


class Card6(Card):
    def __init__(self, group, parent):
        super().__init__(group, 6, parent)
        self.next_stage = 'choice_player'

    def effect(self, player, card, target, number):
        if player != target:
            p_card = player.cards[player.get_index_other_card(card)]
            t_card = target.cards[0]
            p_card.parent = target
            t_card.parent = player
            player.cards[player.get_index_other_card(card)] = t_card
            target.cards[0] = p_card
            if t_card.now_image == 0 and type(player) != Bot:
                t_card.reverse_self()


class Card7(Card):
    def __init__(self, group, parent):
        super().__init__(group, 7, parent)
        self.next_stage = 'next_turn'


class Card8(Card):
    def __init__(self, group, parent):
        super().__init__(group, 8, parent)
        self.next_stage = 'next_turn'

    def effect(self, player, card, target, number):
        self.parent.kill_self()
