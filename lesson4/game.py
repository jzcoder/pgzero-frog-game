#! pgzrun
import pygame
from time import clock as time

WIDTH = 800
HEIGHT = 600
LEAP_FRAME_DELAY = 0.1
MAX_ROWS = 5
MAX_COLS = 6

def scale(actor, factor):
    rect = actor._surf.get_rect()
    new_w = int(rect.width * factor)
    new_h = int(rect.height * factor)
    actor._surf = pygame.transform.smoothscale(actor._surf, (new_w, new_h))
    actor.width, actor.height = actor._surf.get_size()
    actor._calc_anchor()

class Frog(Actor):
    def __init__(self):
        super(Frog, self).__init__('frog_right')
        self.pond_pos = 0, 0

    def jump(self, direction):
        self.image = direction

    def update(self):
        if keyboard.right:
            if self.pond_pos[0] + 1 < MAX_COLS:
                self.pond_pos = self.pond_pos[0] + 1, self.pond_pos[1]
                self.jump('frog_right')
        elif keyboard.left:
            if self.pond_pos[0] - 1 >= 0:
                self.pond_pos = self.pond_pos[0] - 1, self.pond_pos[1]
                self.jump('frog_left')
        elif keyboard.up:
            if self.pond_pos[1] - 1 >= 0:
                self.pond_pos = self.pond_pos[0], self.pond_pos[1] - 1
                self.jump('frog_up')
        elif keyboard.down:
            if self.pond_pos[1] + 1 < MAX_ROWS:
                self.pond_pos = self.pond_pos[0], self.pond_pos[1] + 1
                self.jump('frog_down')

class Pond(object):
    def __init__(self):
        self.lilypads = []
        for y in range(MAX_ROWS):
            row = []
            for x in range(MAX_COLS):
                lilypad = Actor('lilypad_orange')
                lilypad.pos = 100+(x*120), 120+(y*100)

                scale(lilypad, 0.80)
                row.append(lilypad)
            self.lilypads.append(row)

    def draw(self, frog):
        for row in self.lilypads:
            for col in row:
                col.draw()

        lily = self.lilypads[frog.pond_pos[1]][frog.pond_pos[0]]
        frog.x = lily.x
        frog.y = lily.y

        frog.draw()

frog = Frog()
pond = Pond()

def update():
    frog.update()


def draw():
    screen.clear()
    pond.draw(frog)
