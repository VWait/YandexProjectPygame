import pygame.draw

from abstractblock import Block


class Board(Block):
    def __init__(self, size, pos0, props):
        super().__init__(size, pos0, props)

        self.color = (0, 60, 0)

        self.help_blip_size = self.block_size[0] * 0.25, self.block_size[1] * 0.1
        self.help_blip_pos0 = self.block_pos0[0] + 10, self.block_size[1] - self.help_blip_size[1] - 10
        self.help_blip_color = (255, 0, 0)

        self.start_blip_size = self.help_blip_size
        self.start_blip_pos0 = self.block_size[0] - self.help_blip_size[0] - 10, self.help_blip_pos0[1]
        self.start_blip_color = self.help_blip_color

    def render(self, screen):
        super().render(screen)
        pygame.draw.rect(screen, self.help_blip_color, self.help_blip_pos0 + self.help_blip_size)
        pygame.draw.rect(screen, self.start_blip_color, self.start_blip_pos0 + self.start_blip_size)
