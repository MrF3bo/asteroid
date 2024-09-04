# Imports
import pygame
from constants import *
from  player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,)
    asteroidfield = AsteroidField()
    

    # Game loop
    while True:
        # Create functionality to exit out of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                exit()       
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        
        
        # Limiting framerate to 60 fps
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()