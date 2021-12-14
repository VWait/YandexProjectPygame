import pygame
import board


size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True
game_board = board.Board(size)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("black"))
    game_board.render(screen)
    pygame.display.flip()

pygame.quit()
