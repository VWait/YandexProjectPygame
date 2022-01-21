from abc import ABC, abstractmethod

import pygame.draw


class Block(ABC):
    @abstractmethod
    def __init__(self, size, pos0, props):
        self.block_size = size[0] * props[0], size[1] * props[1]
        self.block_pos0 = pos0
        self.color_blip = (0, 0, 0)

    @abstractmethod
    def render(self, screen):
        pygame.draw.rect(screen, self.color_blip, self.block_pos0 + self.block_size)

    def get_xy_by_prop(self, props, size_card):
        return tuple(map(lambda val, p, s: val * p + s / 2, self.block_size, props, size_card))
