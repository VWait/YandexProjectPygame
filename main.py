import pygame
import board
import cards


size = width, height = 800, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
game_board = board.Board(size, (0, 0), (0.75, 1))
all_sprites = pygame.sprite.Group()
for i in range(2):
    cards.Card3(all_sprites, game_board.get_xy_by_prop((0.37 + i * 0.15, 0.7)))
cards.Card6(all_sprites, (20, 60))
cards.Card4(all_sprites, (100, 60))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    game_board.render(screen)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
