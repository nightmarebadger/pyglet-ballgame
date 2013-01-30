import pyglet
from .lists import *
from .screen import *

class Arrow(pyglet.sprite.Sprite):
    def __init__(self, *args, player, speed = 100, **kwargs)
        super().__init__(*args, batch = arrow_batch, **kwargs)
        
        self.speed = speed
        self.player = player
    
        
    def collision_rect(self, other):
        #=======================================================================
        # A simple rectangle collision
        #=======================================================================
        if(self.x <= other.x + other.width/2 and self.x + self.width >= other.x - other.width/2):
            if(self.y <= other.y + other.height/2 and self.y + self.height >= other.y - other.height/2):
                other.hit()
                self.hit()
                
    def hit(self):
        pass
    
    def update(self, dt):
        pass
    
    def destroy(self):
        self.player.arrow = None
        arrow_list.remove(self)
    