import pygame
from pygame import Surface
import numpy as np
import config


def draw_circles(positions: np.typing.NDArray, radius: float, color: tuple, surface: Surface) -> None:
    for x, y in positions:
        pygame.draw.circle(surface, color, (x,y),radius)


#Pygame initialisation
pygame.init()
screen = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption(config.CAPTION)
clock = pygame.time.Clock()
running = True

#Particles
positions = np.random.random((config.PARTICLE_AMOUNT,2))*(config.WIDTH, config.HEIGHT)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255,255,255))
    pygame.display.flip()

    clock.tick(config.FPS_LIMIT)



