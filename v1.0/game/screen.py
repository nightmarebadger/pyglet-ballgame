import pyglet
from . import resources

game_window = pyglet.window.Window(width=800, height=650, caption="Pyglet Ballgame")
window_bottom = 50

background = pyglet.sprite.Sprite(img = resources.background1)

game_over_text = pyglet.text.Label("GAME OVER!", bold = True, font_size=50, anchor_x = "center", anchor_y = "center", x = game_window.width//2, y = game_window.height//2)
game_paused_text = pyglet.text.Label("GAME PAUSED!", bold = True, font_size=50, anchor_x = "center", anchor_y = "center", x = game_window.width//2, y = game_window.height//2)
game_won_text = pyglet.text.Label("GAME WON!", bold = True, font_size=50, anchor_x = "center", anchor_y = "center", x = game_window.width//2, y = game_window.height//2)