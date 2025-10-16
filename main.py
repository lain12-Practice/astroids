import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    print("Starting Asteroids!")
    print("Screen width:",SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()
    shots=pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers=(updatable)
    Shot.containers = (shots, updatable, drawable)
    player_sp=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    ast_field=AsteroidField()
    while(True):
        screen.fill((0,0,0))
        #player_sp.draw(screen)
        dt=clock.tick(60)/1000
        for shape_obj in drawable:
            shape_obj.draw(screen)
     #   player_sp.update(dt)  
        updatable.update(dt)      
        pygame.display.flip()
        for ast in asteroids:
            if(player_sp.colission(ast)):
                print("Game over!")
                return
            for sin_shot in shots:
                if(ast.colission(sin_shot)):
                    ast.split()
                    sin_shot.kill()
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
