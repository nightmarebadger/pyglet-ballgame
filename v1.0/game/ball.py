import pyglet
from . import resources
from .screen import *
from random import randint, choice

class Ball(pyglet.sprite.Sprite):
    def __init__(self, *args, colour, size = None, vx = None, vy = None, rot = None, **kwargs):
        if(colour == 'red'):
            img = resources.ball_red
        elif(colour == 'blue'):
            img = resources.ball_blue
        elif(colour == 'green'):
            img = resources.ball_green
        elif(colour == 'gold'):
            img = resources.ball_gold
            
        super().__init__(img = img, *args, **kwargs)
        
        if(size):
            self.scale = size/self.width
            
        if(not vx):
            self.vx = randint(50, 200) * choice([-1,1])
        else:
            self.vx = vx
        if(not vy):
            self.vy = randint(50, 200) * choice([-1,1])
        else:
            self.vy = vy
            
        if(not rot):
            self.rot = randint(10,30) * choice([-1, 1]) 
        else:
            self.rot = rot
            
    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rotation += self.rot * dt
        
        self.checkBounds()
        
    def checkBounds(self):
        if(self.x - self.width/2 < 0 or self.x + self.width/2 > game_window.width):
            self.vx *= -1

        if(self.y - self.height/2 < window_bottom or self.y + self.height/2 > game_window.height):
            self.vy *= -1
        