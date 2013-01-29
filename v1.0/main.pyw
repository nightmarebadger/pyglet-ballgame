import pyglet
from game.screen import *
from game import player, ball


@game_window.event
def on_draw():
    game_window.clear()
    background.draw()
    ply.draw()
    ball.draw()
    
    
def update(dt):
   ply.update(dt)
   ball.update(dt)


ply = player.Player()
game_window.push_handlers(ply.key_handler)

ball = ball.Ball(colour='red', x = game_window.width/2, y = game_window.height/2, size = 200)

if(__name__ == '__main__'):
  pyglet.clock.schedule_interval(update, 1/120)
  pyglet.app.run()
