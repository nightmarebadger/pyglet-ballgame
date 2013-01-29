import pyglet

pyglet.resource.path = ["../resources/images/player"]
pyglet.resource.reindex()

player1_left = pyglet.resource.image("ply1l.png")
player1_normal = pyglet.resource.image("ply1n.png")
player1_right = pyglet.resource.image("ply1r.png")
player1_shooting = pyglet.resource.image("ply1s.png")
