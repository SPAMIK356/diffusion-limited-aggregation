import pygame
from pygame import Surface
import numpy as np
import config


#Pygame initialisation
pygame.init()
screen = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption(config.CAPTION)
clock = pygame.time.Clock()
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            
    screen.fill((255,255,255))
    pygame.display.flip()

    clock.tick(config.FPS_LIMIT)



