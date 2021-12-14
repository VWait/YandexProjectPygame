from abc import ABC, abstractmethod

import pygame.draw


class Block(ABC):
    @abstractmethod
    def __init__(self, size, pos0, props):
        self.block_size = size[0] * props[0], size[1] * props[1]
        self.block_pos0 = pos0
        self.color = (0, 0, 0)

    @abstractmethod
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.block_pos0 + self.block_size)
