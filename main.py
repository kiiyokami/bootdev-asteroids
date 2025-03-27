import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroid_field import AsteroidField

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt=0
    score=0
    x= SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    
    asteroid_field = AsteroidField()
    player = Player(x,y,PLAYER_RADIUS)

    pygame.display.set_caption("Asteroids")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game Over!\nYou destroyed: {score} asteroids!")
                pygame.quit()
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    score += 1
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = fps.tick(60) / 1000
        
    


if __name__ == "__main__":
    main()