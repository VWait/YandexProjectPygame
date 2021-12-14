import pygame.draw


class Board:
    def __init__(self, size):
        self.board_rect = 0, 0, size[0] * 0.75, size[1]

    def render(self, screen):
        pygame.draw.rect(screen, (20, 20, 20), self.board_rect)
