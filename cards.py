import pygame
from LoadImage import load_image


class Card1(pygame.sprite.Sprite):
    image = load_image('card1.png')

    def __init__(self, group, pos0):
        super().__init__(group)
        self.image = Card1.image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos0
