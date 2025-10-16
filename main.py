import pygame
from constants import *
from player import *
from circleshape import *
def main():
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    updateable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers=(updateable,drawable)
    player_sp=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while(True):
        screen.fill((0,0,0))
        #player_sp.draw(screen)
        dt=clock.tick(60)/1000
        for shape_obj in drawable:
            shape_obj.draw(screen)
     #   player_sp.update(dt)  
        updateable.update(dt)      
        pygame.display.flip()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
