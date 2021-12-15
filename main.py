import pygame
import board
from cards import Card1


size = width, height = 800, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
game_board = board.Board(size, (0, 0), (0.75, 1))
all_sprites = pygame.sprite.Group()
Card1(all_sprites, (0, 0))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    game_board.render(screen)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
