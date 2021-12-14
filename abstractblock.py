from abc import ABC, abstractmethod

import pygame.draw


class Block(ABC):
    @abstractmethod
    def __init__(self, size, x0, y0, prop_x, prop_y):
        self.size_block = size[0] * prop_x, size[1] * prop_y
        self.x0 = x0
        self.y0 = y0
        self.color = (0, 0, 0)

    @abstractmethod
    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.x0, self.y0) + self.size_block)
