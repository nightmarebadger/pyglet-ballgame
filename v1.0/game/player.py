import pyglet
from pyglet.window import key
from game import globals
from .screen import *
from .lists import *
from . import resources, arrow
from time import sleep


class Player(pyglet.sprite.Sprite):
    def __init__(self, *args, speed = 300, **kwargs):
        super().__init__(*args, img = resources.player1_normal, batch = player_batch, **kwargs)
        
        #self.image = 
        self.x = game_window.width/2 - self.width/2
        self.y = window_bottom
        
        self.speed = speed
        self.vx = 0
        self.key_handler = key.KeyStateHandler()
        
        self.shooting = False
        
        self.arrow = None
        
    def draw(self):
        self.draw()
        if(self.arrow):
            self.arrow.draw()
        
    def update(self, dt):
        self.keys()
        self.changeImg()
        self.move(dt)
        self.checkBounds()
        
    def move(self, dt):
        self.x += self.vx * dt
    
    def on_key_press(self, symbol, modifiers):
        if(symbol == key.P):
            #===================================================================
            # if(globals.game_paused):
            #    # Take 3 seconds to unpause or sth
            #===================================================================
            globals.game_paused = not globals.game_paused
             

                                
    def keys(self):
        self.vx = 0
        if(self.key_handler[key.SPACE]):
            self.shooting = True
            self.shoot()
        else:
            self.shooting = False
            self.stopShoot()
            
        if(not self.shooting):
            if(self.key_handler[key.LEFT]):
                self.vx -= self.speed
            if(self.key_handler[key.RIGHT]):
                self.vx += self.speed
    
    def changeImg(self):
        if(self.shooting):
            self.image = resources.player1_shooting
        else:
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
            
    def collision_rect(self, other):
        #=======================================================================
        # A simple rectangle collision
        #=======================================================================
        if(self.x <= other.x + other.width/2 and self.x + self.width >= other.x - other.width/2):
            if(self.y <= other.y + other.height/2 and self.y + self.height >= other.y - other.height/2):
                other.hit()
                self.hit()
    
    def hit(self):
        self.destroy()
        
    def destroy(self):
        player_list.remove(self)
    
    def shoot(self):
        if(not self.arrow):
            self.arrow = arrow.Arrow(player = self)
            arrow_list.append(self.arrow)
    
    def stopShoot(self):
        if(self.arrow):
            self.arrow.destroy()
        