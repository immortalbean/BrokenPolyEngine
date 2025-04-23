import pygame

pygame.init()
resolution = (1280, 720)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

def start():
    while True:
        if pygame.event.get(pygame.QUIT): break
        clock.tick(60)
    pygame.quit()