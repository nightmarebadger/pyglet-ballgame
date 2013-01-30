import pyglet
from pyglet.window import key
from .screen import *
from .lists import *
from . import resources


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, img = resources.player1_normal, batch = player_batch, **kwargs)
        
        #self.image = 
        self.x = game_window.width/2 - self.width/2
        self.y = window_bottom
        
        self.speed = 300
        self.vx = 0
        self.key_handler = key.KeyStateHandler()
        
    def update(self, dt):
        self.keys()
        self.changeImg()
        self.move(dt)
        self.checkBounds()
        
    def move(self, dt):
        self.x += self.vx * dt
            
    def keys(self):
        self.vx = 0
        if(self.key_handler[key.LEFT]):
            self.vx -= self.speed
        if(self.key_handler[key.RIGHT]):
            self.vx += self.speed
    
    def changeImg(self):
        if(self.vx < 0):
            self.image = resources.player1_left
        elif(self.vx > 0):
            self.image = resources.player1_right
        elif(self.vx == 0):
            self.image = resources.player1_normal
            
    def checkBounds(self):
        if(self.x < 0):
            self.x = 0
        elif(self.x + self.width > game_window.width):
            self.x = game_window.width - self.width
            
    def collision(self, other):
        #=======================================================================
        # A simple rectangle collision
        #=======================================================================
        if(self.x <= other.x + other.width/2 and self.x + self.width >= other.x - other.width/2):
            if(self.y <= other.y + other.height/2 and self.y + self.height >= other.y - other.height/2):
                print("Collision detected!")
        
        