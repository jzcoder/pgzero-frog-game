#! pgzrun
WIDTH = 800
HEIGHT = 600

frog = Actor('frog')
frog.pos = 100, HEIGHT-100

def update():
    if keyboard.right:
        frog.x += 20
    elif keyboard.left:
        frog.x -= 20
    elif keyboard.up:
        frog.y -= 20
    elif keyboard.down:
        frog.y += 20

def draw():
    screen.clear()
    frog.draw()
