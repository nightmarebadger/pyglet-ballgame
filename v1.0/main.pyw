import pyglet
from game.screen import *
from game.lists import *
from game import utility, player, ball


@game_window.event
def on_draw():
    game_window.clear()
    background.draw()
    player_batch.draw()
    ball_batch.draw()
    fps_display.draw()
    
    
def update(dt):
    for ply in player_list:
        ply.update(dt)
    for ball in ball_list:
        ball.update(dt)
        for ply in player_list:
            ply.collision_rect(ball)


player_list.append(player.Player())
game_window.push_handlers(player_list[-1].key_handler)
#utility.addBalls(40)

fps_display = pyglet.clock.ClockDisplay(format='%(fps).1f', color=(0.5, 0.5, 0.5, 1))

ball_list.append(ball.Ball(colour = "red", x = 200, y = 200, size = 100, split_times = 1, split_into = 12))

if(__name__ == '__main__'):
  pyglet.clock.schedule_interval(update, 1/120)
  pyglet.app.run()
