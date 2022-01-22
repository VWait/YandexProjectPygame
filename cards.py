import pygame.draw

from spriteclass import Sprite


class Card(Sprite):
    def __init__(self, group, value, pos0):
        super().__init__(group)
        self.value = value
        self.image = self.load_image(f'card{self.value}.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos0
        self.clicked = 0

    def click(self, screen):
        self.clicked = (self.clicked + 1) % 2
        if celf.clicked == 1:
            self.contour_card(screen)
        else:
            self.move()

    def contour_card(self, screen):
        block_pos0 = self.rect.x - 3, self.rect.y - 3
        block_size_window = self.block_pos0[0] + self.rect[2] + 6, self.block_pos0[1] + self.rect[3] + 6
        pygame.draw.rect(screen, (255, 255, 255), block_pos0 + block_size_window, width=3)


class Card1(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 1, pos0)


class Card2(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 2, pos0)


class Card3(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 3, pos0)


class Card4(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 4, pos0)


class Card5(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 5, pos0)


class Card6(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 6, pos0)


class Card7(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 7, pos0)


class Card8(Card):
    def __init__(self, group, pos0):
        super().__init__(group, 8, pos0)
