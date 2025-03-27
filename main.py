import pygame
from constants import *
from player import Player

def main():
    fps = pygame.time.Clock()
    dt=0
    x= SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    player = Player(x,y,PLAYER_RADIUS)
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000
        
    


if __name__ == "__main__":
    main()