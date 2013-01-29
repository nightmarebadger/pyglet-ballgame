import pyglet


#===============================================================================
# PLAYER IMAGES
#===============================================================================

pyglet.resource.path = ["../resources/images/player"]
pyglet.resource.reindex()

player1_left = pyglet.resource.image("ply1l.png")
player1_normal = pyglet.resource.image("ply1n.png")
player1_right = pyglet.resource.image("ply1r.png")
player1_shooting = pyglet.resource.image("ply1s.png")

player2_left = pyglet.resource.image("ply2l.png")
player2_normal = pyglet.resource.image("ply2n.png")
player2_right = pyglet.resource.image("ply2r.png")
player2_shooting = pyglet.resource.image("ply2s.png")

#===============================================================================
# BALL IMAGES
#===============================================================================

pyglet.resource.path = ["../resources/images/ball"]
pyglet.resource.reindex()

ball_blue = pyglet.resource.image("blue.png")
ball_gold = pyglet.resource.image("gold.png")
ball_green = pyglet.resource.image("green.png")
ball_red = pyglet.resource.image("red.png")

#===============================================================================
# BACKGROUND IMAGES
#===============================================================================

pyglet.resource.path = ["../resources/images/background"]
pyglet.resource.reindex()

background1 = pyglet.resource.image("1.png")
background2 = pyglet.resource.image("2.png")
background3 = pyglet.resource.image("3.png")
background4 = pyglet.resource.image("4.png")
