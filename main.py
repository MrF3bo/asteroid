# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    # Game loop
    while True:
        # Create functionality to exit out of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Creating a window with a black background
        screen.fill((0,0,0))
        pygame.display.flip()
        
        # Limiting framerate to 60 fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()