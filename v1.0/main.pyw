import pyglet
from game.screen import *
from game.lists import *
from game import utility, player


@game_window.event
def on_draw():
    game_window.clear()
    background.draw()
    player_batch.draw()
    ball_batch.draw()
    
    
def update(dt):
    for ply in player_list:
        ply.update(dt)
    for ball in ball_list:
        ball.update(dt)


player_list.append(player.Player())
game_window.push_handlers(player_list[-1].key_handler)
utility.addBalls(40)

if(__name__ == '__main__'):
  pyglet.clock.schedule_interval(update, 1/120)
  pyglet.app.run()
