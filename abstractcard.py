from abc import ABC, abstractmethod

import pygame.draw

import LoadImage


class Card(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def move(self):
        pass
