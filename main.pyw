import pyglet


game_window = pyglet.window.Window(width=800, height=600)

@game_window.event
def on_draw():
    game_window.clear()
    
    
def update(dt):
    pass

if(__name__ == '__main__'):
    pyglet.clock.schedule_interval(update, 1/120)
    pyglet.app.run()

#test2