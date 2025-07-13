import pygame
from pygame import Surface
import numpy as np
from numpy.typing import NDArray
import config

def draw_grid(grid: NDArray, width, height) -> Surface:
    '''Generate a surface with grid and scales it to width and height'''
    sim_surface = Surface(grid.shape)

    colored_grid = np.full((grid.shape[0],grid.shape[1],3), (0,0,0))
    colored_grid[grid] = (255,255,255)

    pygame.surfarray.blit_array(sim_surface,colored_grid)
    scaled_surface = pygame.transform.scale(sim_surface, (width, height))
    return scaled_surface

def wrap(positions: np.typing.NDArray, x_limit:float, y_limit:float) -> None:
    positions[positions[:,0]>x_limit-2,0] = 1
    positions[positions[:,0]<1,0] = x_limit-2
    positions[positions[:,1]>y_limit-2,1] = 1
    positions[positions[:,1]<1,1] = y_limit-2

def find_neighbours(is_stuck : NDArray, walkers : NDArray):
    have_neigbours = np.full(walkers.shape[0], False)
    for a in [-1,0,1]:
        for b in [-1,0,1]:
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
is_stuck = np.full((config.SIM_WIDTH, config.SIM_HEIGHT),False)
is_stuck[int(config.SIM_WIDTH/2), int(config.SIM_HEIGHT/2)] = True
walkers = np.random.randint(1, config.SIM_WIDTH-1, (config.PARTICLE_AMOUNT, 2))
velocities = np.random.randint(-1, 2, (config.PARTICLE_AMOUNT, 2))
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            image_surface = Surface(is_stuck.shape)

            colored_pixels = np.full((is_stuck.shape[0], is_stuck.shape[1], 3), (0,0,0))
            colored_pixels[is_stuck] = (255,255,255)
            pygame.surfarray.blit_array(image_surface, colored_pixels)
            pygame.image.save(image_surface,'image.png')
            running = False

    
    have_neigbours = find_neighbours(is_stuck,walkers)

    is_stuck[walkers[have_neigbours,0], walkers[have_neigbours,1]] = True

    screen.fill((255,255,255))
    
    screen.blit(draw_grid(is_stuck,config.WIDTH,config.HEIGHT), (0,0))

    pygame.display.flip()

    walkers = walkers[np.logical_not(have_neigbours)]
    velocities = velocities[np.logical_not(have_neigbours)]
    walkers+=velocities
    wrap(walkers, config.SIM_WIDTH, config.SIM_HEIGHT)
    clock.tick(config.FPS_LIMIT)

    



