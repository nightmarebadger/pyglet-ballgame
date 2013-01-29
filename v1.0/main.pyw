import pyglet
from game.screen import *
from game import player


@game_window.event
def on_draw():
    game_window.clear()
    background.draw()
    ply.draw()
    
    
def update(dt):
   ply.update(dt)


ply = player.Player()
game_window.push_handlers(ply.key_handler)

if(__name__ == '__main__'):
  pyglet.clock.schedule_interval(update, 1/120)
  pyglet.app.run()
