import pyglet
from game.screen import *


@game_window.event
def on_draw():
    game_window.clear()
    
    
def update(dt):
    pass

if(__name__ == '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()