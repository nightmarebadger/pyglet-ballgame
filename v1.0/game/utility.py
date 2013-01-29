import pyglet
from . import ball
from .lists import *
from .screen import *
from random import randint, choice

def addBalls(n):
   for i in range(n):
       foo = randint(50, 200)
       ball_list.append(ball.Ball(colour=choice(['red', 'green', 'blue']), x = randint(foo//2, game_window.width-foo//2), y = randint(game_window.height//3 + foo//2, game_window.height - foo//2), size = foo))
