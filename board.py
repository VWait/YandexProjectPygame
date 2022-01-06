import pygame.draw

from abstractblock import Block

pygame.font.init()


class Board(Block):
    def __init__(self, size, pos0, props):
        super().__init__(size, pos0, props)

        self.color_blip = (175, 214, 255)
        self.color_letter = (255, 255, 255)
        self.size_letter = 20

        self.help_blip_size = self.block_size[0] * 0.26, self.block_size[1] * 0.1
        self.help_blip_pos0 = self.block_pos0[0] + 10, self.block_size[1] - self.help_blip_size[1] - 10
        self.help_blip_color = (58, 144, 255)

        self.start_blip_size = self.help_blip_size
        self.start_blip_pos0 = self.block_size[0] - self.help_blip_size[0] - 10, self.help_blip_pos0[1]
        self.start_blip_color = self.help_blip_color

    def render(self, screen):
        super().render(screen)
        font = pygame.font.SysFont('cambria', self.size_letter)
        text1 = font.render('Какие карты остались:', True, self.color_letter)
        text2 = font.render('Стражница - 0   Священник - 0   Барон - 0         Служанка - 0', True, self.color_letter)
        text3 = font.render('Принц - 0             Король - 0             Графиня - 0   Принцесса - 0', True,
                            self.color_letter)
        screen.blit(text1, (0, -5))
        screen.blit(text2, (0, self.size_letter - 5))
        screen.blit(text3, (0, self.size_letter * 2 - 5))
        pygame.draw.rect(screen, self.help_blip_color, self.help_blip_pos0 + self.help_blip_size)
        pygame.draw.rect(screen, self.start_blip_color, self.start_blip_pos0 + self.start_blip_size)
        font = pygame.font.SysFont('comic sans', self.size_letter)
        text4 = font.render('Сходить левой', True, self.color_letter)
        text5 = font.render('Сходить правой', True, self.color_letter)
        text6 = font.render('картой', True, self.color_letter)
        screen.blit(text4, self.help_blip_pos0)
        screen.blit(text6, (self.help_blip_pos0[0] + 35, self.help_blip_pos0[1] + 17))
        screen.blit(text5, self.start_blip_pos0)
        screen.blit(text6, (self.start_blip_pos0[0] + 35, self.start_blip_pos0[1] + 17))