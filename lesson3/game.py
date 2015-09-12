#! pgzrun
import pygame

WIDTH = 800
HEIGHT = 600

class Frog(Actor):
    def __init__(self):
        super(Frog, self).__init__('frog_right')
        self.pos = 100, HEIGHT-100

    def jump(self, direction):
        self.image = direction

    def update(self):
        if keyboard.right:
            self.x += 20
            self.jump('frog_right')
        elif keyboard.left:
            self.x -= 20
            self.jump('frog_left')
        elif keyboard.up:
            self.y -= 20
            self.jump('frog_up')
        elif keyboard.down:
            self.y += 20
            self.jump('frog_down')

frog = Frog()

def update():
    frog.update()


def draw():
    screen.clear()
    frog.draw()
