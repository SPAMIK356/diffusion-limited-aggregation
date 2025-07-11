import pygame
from pygame import Surface
import numpy as np
from numpy.typing import NDArray
import config

def draw_grid(grid: NDArray, sim_surface: Surface, width, height) -> Surface:
    '''Generate a surface with grid and scales it to width and height'''
    pygame.surfarray.blit_array(sim_surface,grid)
    scaled_surface = pygame.transform.scale(sim_surface, (width, height))
    return scaled_surface

def find_neighbours(is_stuck : NDArray, walkers : NDArray):
    have_neigbours = np.full(walkers.shape[0], False)
    for a in range(-1, 2):
        for b in range(-1,2):
            if a == 0 and b == 0:
                continue
            have_neigbours += is_stuck[walkers[:,0]+a, walkers[:,1]+b]
    return have_neigbours

#Pygame initialisation
pygame.init()
screen = pygame.display.set_mode((config.WIDTH,config.HEIGHT))
pygame.display.set_caption(config.CAPTION)
clock = pygame.time.Clock()
running = True

#Particles
is_stuck = np.full((config.WIDTH, config.HEIGHT),False)
is_stuck[int(config.WIDTH/2), int(config.HEIGHT/2)] = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    walkers = np.random.randint(0, config.WIDTH, (config.PARTICLE_AMOUNT, 2))
    print(find_neighbours(is_stuck, walkers))
    screen.fill((255,255,255))
    #render here

    pygame.display.flip()

    



