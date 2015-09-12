#! pgzrun
import pygame
from time import time
from random import random, randint

WIDTH = 800
HEIGHT = 600
LEAP_FRAME_DELAY = 0.1
MAX_ROWS = 5
MAX_COLS = 6

def scale(actor, factor):
    surf = actor.orig_surf or actor._surf
    rect = surf.get_rect()
    new_w = int(rect.width * factor)
    new_h = int(rect.height * factor)
    actor._surf = pygame.transform.smoothscale(surf, (new_w, new_h))
    actor.width, actor.height = actor._surf.get_size()
    actor.center = (actor.x, actor.y)
    actor._calc_anchor()

def restore_surface(actor, orig_surf):
    actor._surf = orig_surf
    actor.width, actor.height = actor._surf.get_size()
    actor.center = (actor.x, actor.y)
    actor._calc_anchor()


class Frog(Actor):
    def __init__(self):
        super(Frog, self).__init__('frog_right')
        self.pond_pos = 0, 0
        self.key_pressed = None

    def jump(self, direction):
        self.image = direction

    def update(self):
        for key in [keys.RIGHT, keys.LEFT, keys.UP, keys.DOWN]:
            if keyboard[key]:
                self.key_pressed = key
                return

        if self.key_pressed == keys.RIGHT:
            if self.pond_pos[0] + 1 < MAX_COLS:
                self.pond_pos = self.pond_pos[0] + 1, self.pond_pos[1]
                self.jump('frog_right')
        elif self.key_pressed == keys.LEFT:
            if self.pond_pos[0] - 1 >= 0:
                self.pond_pos = self.pond_pos[0] - 1, self.pond_pos[1]
                self.jump('frog_left')
        elif self.key_pressed == keys.UP:
            if self.pond_pos[1] - 1 >= 0:
                self.pond_pos = self.pond_pos[0], self.pond_pos[1] - 1
                self.jump('frog_up')
        elif self.key_pressed == keys.DOWN:
            if self.pond_pos[1] + 1 < MAX_ROWS:
                self.pond_pos = self.pond_pos[0], self.pond_pos[1] + 1
                self.jump('frog_down')

        self.key_pressed = None

class Lilypad(Actor):
    DECAY_SCALES = [0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0]
    FINAL_DECAY = len(DECAY_SCALES)-1

    def __init__(self, image):
        super(Lilypad, self).__init__(image)
        self.orig_surf = self._surf
        self.delay_rate = 0.5 + (random() * 3)
        self.reset_rate = 1.0 + (random() * 5)
        self.decay_pos = randint(0, Lilypad.FINAL_DECAY)
        self.update()

    def reset(self):
        restore_surface(self, self.orig_surf)
        self.decay_pos = -1
        self.update()

    def update(self):
        if self.decay_pos == Lilypad.FINAL_DECAY:
            self.state = 'missing'
            clock.schedule(self.reset, self.reset_rate)
        else:
            self.decay_pos += 1

            if self.decay_pos == Lilypad.FINAL_DECAY:
                self.state = 'missing'
            else:
                self.state = 'available'

            clock.schedule(self.update, self.delay_rate)

        scale(self, Lilypad.DECAY_SCALES[self.decay_pos])


class Pond(object):
    def __init__(self):
        self.lilypads = []
        for y in range(MAX_ROWS):
            row = []
            for x in range(MAX_COLS):
                lilypad = Lilypad('lilypad_orange')
                lilypad.pos = 100+(x*120), 120+(y*100)

                #scale(lilypad, lilypad.scale)

                row.append(lilypad)
            self.lilypads.append(row)

    def update(self):
        lily = self.lilypads[frog.pond_pos[1]][frog.pond_pos[0]]
        frog.x = lily.x
        frog.y = lily.y

    def draw(self, frog):
        for row in self.lilypads:
            for col in row:
                col.draw()

        frog.draw()

frog = Frog()
pond = Pond()

def update():
    frog.update()
    pond.update()

def draw():
    screen.clear()
    pond.draw(frog)
