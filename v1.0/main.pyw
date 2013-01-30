import pyglet
from game.screen import *
from game.lists import *
from game import utility, player, ball, arrow
from pyglet import gl


@game_window.event
def on_draw():
    game_window.clear()
    background.draw()
    player_batch.draw()
    ball_batch.draw()
    #===========================================================================
    # arrow_batch.draw()
    #===========================================================================
    for i in arrow_list:
      i.draw()
    fps_display.draw()
    
    
def update(dt):
    for ply in player_list:
        ply.update(dt)
    for ball in ball_list:
        ball.update(dt)
        for ply in player_list:
            ply.collision_rect(ball)
        for arrow in arrow_list:
           arrow.collision_rect(ball)
    for arrow in arrow_list:
        arrow.update(dt)


player_list.append(player.Player())
game_window.push_handlers(player_list[-1].key_handler)
utility.addBalls(3)

fps_display = pyglet.clock.ClockDisplay(format='%(fps).1f', color=(0.5, 0.5, 0.5, 1))



if(__name__ == '__main__'):
  pyglet.clock.schedule_interval(update, 1/120)
  pyglet.app.run()
