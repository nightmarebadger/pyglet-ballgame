import pyglet
from . import resources
from .screen import *
from .lists import *
from random import randint, choice

class Ball(pyglet.sprite.Sprite):
    def __init__(self, *args, colour, size = None, vx = None, vy = None, rot = None, split_times = 0, split_into = 0, **kwargs):
        if(colour == 'red'):
            img = resources.ball_red
        elif(colour == 'blue'):
            img = resources.ball_blue
        elif(colour == 'green'):
            img = resources.ball_green
        elif(colour == 'gold'):
            img = resources.ball_gold
            
        super().__init__(*args, img = img, batch = ball_batch, **kwargs)
        
        self.colour = colour
        
        self.size = None
        if(size):
            self.scale = size/self.width
            self.size = size
        else:
            self.size = self.width
            
        if(not vx):
            self.vx = randint(50, 200) * choice([-1,1])
        else:
            self.vx = vx
        if(not vy):
            self.vy = randint(50, 200) * choice([-1,1])
        else:
            self.vy = vy
            
        if(not rot):
            self.rot = randint(100,200) * choice([-1, 1]) 
        else:
            self.rot = rot
            
        self.split_times = split_times
        self.split_into = split_into
            
    def update(self, dt):
        self.vy -= gravity * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rotation += self.rot * dt
        
        self.checkBounds()
        
    def checkBounds(self):
        if(self.x - self.width/2 < 0):
            self.x = self.width/2
            self.vx *= -1
            self.rot *= -1
        if(self.x + self.width/2 > game_window.width):
            self.x = game_window.width - self.width/2
            self.vx *= -1
            self.rot *= -1

        if(self.y - self.height/2 < window_bottom):
            self.y = window_bottom + self.height/2
            self.vy *= -1
            self.rot *= -1
        if(self.y + self.height/2 > game_window.height):
            self.y = game_window.height - self.height/2
            self.vy *= -1
            self.rot *= -1
    
    def destroy(self):
        ball_list.remove(self)
        
    def hit(self):
        if(self.split_times > 0):
            self.split()
        self.destroy()
        
    def split(self):
        if(self.split_times >= 0):
            for i in range(self.split_into):
                ball_list.append(Ball(colour=self.colour, x = self.x + randint(-self.width//2, self.width//2), y = self.y + randint(-self.height//2, self.height//2), size = self.size/(2)**(1/2), vx = self.vx + randint(min(-self.vx//2, self.vx//2), max(-self.vx//2, self.vx//2)), vy = self.vy + randint(min(-self.vy//2, self.vy//2), max(-self.vy//2, self.vy//2)), split_into = self.split_into, split_times = self.split_times - 1))