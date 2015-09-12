#! pgzrun
WIDTH = 800
HEIGHT = 600

frog = Actor('frog')
frog.pos = 100, HEIGHT-100

def draw():
    screen.clear()
    frog.draw()
