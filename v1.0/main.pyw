import pyglet
from game.screen import *
from game.lists import *
from game import globals
from game import utility, player, ball, arrow
from pyglet import gl


@game_window.event
def on_draw():
    game_window.clear()
    if(globals.game_over):
        game_over_text.draw()
        return
    if(globals.game_won):
        print("Gamuh is won!")
        game_won_text.draw() 
        return
    if(globals.game_paused):
        game_paused_text.draw()
        return
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
    if(not player_list):
        globals.game_over = True
        return
    if(not ball_list):
        globals.game_won = True
        return
    if(globals.game_paused):
        return
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
game_window.push_handlers(player_list[-1])
utility.addBalls(1)

fps_display = pyglet.clock.ClockDisplay(format='%(fps).1f', color=(0.5, 0.5, 0.5, 1))



if(__name__ == '__main__'):
  pyglet.clock.schedule_interval(update, 1/120)
  pyglet.app.run()
