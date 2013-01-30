import pyglet
from .lists import *
from .screen import *
from . import resources
from pyglet import gl

class Arrow(pyglet.sprite.Sprite):
    def __init__(self, *args, player, speed = 300, **kwargs):
        super().__init__(*args, img = resources.ost1, batch = arrow_batch, **kwargs)
        
        self.speed = speed
        self.player = player
        self._width = 5
        self._height = 1
    
        
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
        self._height += self.speed * dt
    
    def destroy(self):
        arrow_list.remove(self)
        
    def draw(self):
        gl.glColor3f(0,0,0)
        
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2f', (self.player.x + self.player.width//2 - self._width//2, self.player.y + self.player.height,
                 self.player.x + self.player.width//2 - self._width//2, self.player.y + self.player.height + self._height,
                 self.player.x + self.player.width//2 + self._width//2, self.player.y + self.player.height + self._height,
                 self.player.x + self.player.width//2 + self._width//2, self.player.y + self.player.height))
        )
    