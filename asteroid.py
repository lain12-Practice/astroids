import pygame
import random
from circleshape import CircleShape
from constants import *
class Asteroid(CircleShape):
    #containers=[]
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self, dt):
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if(self.radius<ASTEROID_MIN_RADIUS):
            return
        angle=random.uniform(20,50)
        vol1=self.velocity.rotate(angle)*1.2
        vol2=self.velocity.rotate(-1*angle)
        new_rad=self.radius-ASTEROID_MIN_RADIUS
        ast1=Asteroid(self.position[0],self.position[1],new_rad)
        ast2=Asteroid(self.position[0],self.position[1],new_rad)
        ast1.velocity=vol1
        ast2.velocity=vol2
        