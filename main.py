import pygame
from constants import *
from player import Player

def main():
    fps = pygame.time.Clock()
    dt=0
    x= SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    player = Player(x,y,PLAYER_RADIUS)
    


    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}\n")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.init()
    while True:
        screen.fill("black")

        player.update(dt)
        player.draw(screen)
        player.move(PLAYER_TURN_SPEED * dt)
        
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()



if __name__ == "__main__":
    main()