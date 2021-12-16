import pygame
import board
from cards import Card


size = width, height = 800, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
game_board = board.Board(size, (0, 0), (0.75, 1))
all_sprites = pygame.sprite.Group()
for i in range(2):
    Card(all_sprites, 'card1.png', game_board.get_xy_by_prop((0.35 + i * 0.15, 0.7)))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    game_board.render(screen)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
