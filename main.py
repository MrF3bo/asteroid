# Imports
import pygame
from constants import *
from  player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0
    scorefont = pygame.font.Font(None, 36)

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,)
    asteroidfield = AsteroidField()
    

    # Game loop
    while True:
        # Create functionality to exit out of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        # Display score
        score_text = scorefont.render(f'Score: {score}', True, (255,255,255))
        screen.blit(score_text, (10,10))

        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    # Scoring system
                    if asteroid.radius == 20:
                        score += 25
                    elif asteroid.radius == 40:
                        score += 100
                    elif asteroid.radius == 60:
                        score += 250
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