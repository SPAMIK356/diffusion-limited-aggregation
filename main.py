import pygame
from pygame import Surface
import numpy as np
import config


def draw_circles(positions: np.typing.NDArray, radius: float, color: tuple, surface: Surface) -> None:
    for x, y in positions:
        pygame.draw.circle(surface, color, (x,y),radius)

def wrap(positions: np.typing.NDArray, x_limit:float, y_limit:float, offset:float):
    positions[positions[:,0]>x_limit+offset,0] = -offset
    positions[positions[:,0]<-offset,0] = x_limit+offset
    positions[positions[:,1]>y_limit+offset,1] = -offset
    positions[positions[:,1]<-offset,1] = y_limit+offset

#Pygame initialisation
pygame.init()
screen = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption(config.CAPTION)
clock = pygame.time.Clock()
running = True

#Particles
positions = np.random.random((config.PARTICLE_AMOUNT,2))*(config.WIDTH, config.HEIGHT)
velocities = np.random.random(positions.shape)*config.SPEED_MULTIPLIER
is_stuck = np.full(config.PARTICLE_AMOUNT,False)
is_stuck[0] = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    draw_circles(positions,config.RADIUS, config.COLOR, screen)

    pygame.display.flip()

    
    deltaTime = clock.tick(config.FPS_LIMIT) / 1000.0

    velocities[is_stuck] = 0
    print(velocities)
    positions+= velocities*deltaTime
    
    velocities*= config.DAMPING

    wrap(positions, config.WIDTH, config.HEIGHT, config.RADIUS)
    



