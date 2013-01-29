import pyglet
from . import resources

game_window = pyglet.window.Window(width=800, height=650, caption="Pyglet Ballgame")
window_bottom = 50

background = pyglet.sprite.Sprite(img = resources.background_image1)