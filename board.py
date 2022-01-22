import pygame.draw
import math

from abstractblock import Block

pygame.font.init()


class Board(Block):
    def __init__(self, size, pos0, props):
        super().__init__(size, pos0, props)
        self.block_size_main = size
        self.block_size = size[0] * props[0], size[1] * props[1]
        self.block_size_window = size[0] * props[0] * 0.4, size[1] * props[1] * 0.3
        self.block_pos0 = pos0
        self.color_blip = (175, 214, 255)
        self.color_letter = (255, 255, 255)
        self.size_letter = 20
        distance_border = 35

        self.help_blip_size = self.block_size[0] * 0.25, self.block_size[1] * 0.1
        self.help_blip_pos0 = self.block_pos0[0] + 10, self.block_size[1] - self.help_blip_size[1] - 10
        self.help_blip_color = (113, 130, 255)

        self.start_blip_size = self.help_blip_size
        self.start_blip_pos0 = self.block_size[0] - self.help_blip_size[0] - 10, self.help_blip_pos0[1]
        self.start_blip_color = self.help_blip_color

        self.first_player = PlayerHand(self.block_size_window,
                                       (self.block_pos0[0] + distance_border, self.block_pos0[1] + distance_border))
        self.second_player = PlayerHand(self.block_size_window,
                                        (self.block_size[0] - distance_border - self.block_size_window[0],
                                         self.block_pos0[1] + distance_border))
        self.third_player = PlayerHand(self.block_size_window,
                                       (self.block_pos0[0] + self.block_size[0] / 2 - self.block_size_window[0] / 2,
                                        self.block_pos0[1] + distance_border * 2 + self.block_size_window[1]))

    def render(self, screen):
        super().render(screen)
        self.first_player.render(screen)
        # self.first_player.contour_window(screen)
        self.second_player.render(screen)
        self.third_player.render(screen)
        font = pygame.font.SysFont('cambria', self.size_letter)
        text1 = font.render('Какие карты остались:', True, self.color_letter)
        text2 = font.render('Стражница - 0   Священник - 0   Барон - 0         Служанка - 0', True, self.color_letter)
        text3 = font.render('Принц - 0             Король - 0             Графиня - 0   Принцесса - 0', True,
                            self.color_letter)
        # screen.blit(text1, (0, -5))
        # screen.blit(text2, (0, self.size_letter - 5))
        # screen.blit(text3, (0, self.size_letter * 2 - 5))
        pygame.draw.rect(screen, self.help_blip_color, self.help_blip_pos0 + self.help_blip_size)
        pygame.draw.rect(screen, self.start_blip_color, self.start_blip_pos0 + self.start_blip_size)
        font = pygame.font.SysFont('comic sans', self.size_letter)
        text4 = font.render('Сходить левой', True, self.color_letter)
        text5 = font.render('Сходить правой', True, self.color_letter)
        text6 = font.render('картой', True, self.color_letter)
        # screen.blit(text4, self.help_blip_pos0)
        # screen.blit(text6, (self.help_blip_pos0[0] + 35, self.help_blip_pos0[1] + 17))
        # screen.blit(text5, self.start_blip_pos0)
        # screen.blit(text6, (self.start_blip_pos0[0] + 35, self.start_blip_pos0[1] + 17))


class PlayerHand(Block): 
    def __init__(self, size, pos0):
        super().__init__(size, pos0, (1, 1))
        self.block_size_window = size
        self.block_pos0 = pos0
        self.color_window = (113, 130, 255)
        self.color_name = (205, 255, 255)
        self.name_window = self.block_size_window[0], self.block_size_window[1] / 6

    def render(self, screen):
        super().render(screen)
        pygame.draw.rect(screen, self.color_window, self.block_pos0 + self.block_size_window)
        pygame.draw.rect(screen, self.color_name, self.block_pos0 + self.name_window)
        # self.cards_played(screen, [1, 1, 1, 1, 1])

    def contour_window(self, screen):
        block_pos0 = self.block_pos0[0] - 3, self.block_pos0[1] - 3
        block_size_window = self.block_size_window[0] + 6, self.block_size_window[1] + 6
        pygame.draw.rect(screen, (255, 255, 255), block_pos0 + block_size_window, width=3)

    def get_pos0(self, n):
        ratio = (3.5, 1.55, 4)
        cards = [(self.block_pos0[0] + self.block_size_window[0] / ratio[i],
                  self.block_pos0[1] + self.block_size_window[1] / ratio[2]) for i in range(1, n + 1)]
        return cards

    def cards_played(self, screen, cards):
        radius = 12.5
        ratio = (6, 5)
        pos0 = (35, 60)
        count_card = 0
        for i in range(math.ceil(len(cards) / 2)):
            for j in range(2):
                count_card += 1
                pygame.draw.circle(screen, (255, 255, 255), (pos0[0] + (ratio[0] + radius) * (j + 1) + radius * j,
                                                             pos0[1] + (ratio[1] + radius) * (i + 1) + radius * i),
                                   radius, 0)
                if count_card == len(cards):
                    break