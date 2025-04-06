import sys
import pygame
from constants import *
from asteroidfield import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from sys import exit

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    spawn_x = SCREEN_WIDTH / 2
    spawn_y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(spawn_x, spawn_y, shots)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000
   
    
if __name__ == "__main__":
    main()