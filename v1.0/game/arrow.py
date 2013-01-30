import pyglet

class Arrow(pyglet.sprite.Sprite):
    def __init__(self, *args, speed = 100, **kwargs)
        super().__init__(*args, **kwargs)
        
        self.speed = speed