import pygame
import sys

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tables")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cell = Cell(100, 100, 100, "lh", 30)

    pygame.display.flip()

pygame.quit()
sys.exit()