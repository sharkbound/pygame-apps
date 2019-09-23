from random import randint

from pygame import display as dsp, event as ev, draw as dr, key, locals
from pygame.colordict import THECOLORS as COLORS
import pygame as py

SIZE = (600, 600)
py.init()
dsp.init()
S = dsp.set_mode(SIZE)


def main():
    running = True
    while running:
        for e in ev.get():
            if e.type == py.QUIT or e.type == py.KEYDOWN and e.key == locals.K_ESCAPE:
                py.quit()
                quit()

            if e.type == py.MOUSEBUTTONDOWN:
                Seeker().draw()

        dsp.update()


class Seeker:
    def __init__(self, x=None, y=None):
        self.x = x if x else randint(0, SIZE[0])
        self.y = y if y else randint(0, SIZE[1])
        self.angle = 0

    @property
    def pos(self):
        return self.x, self.y

    def draw(self, size=5):
        dr.circle(S, COLORS['red'], self.pos, size)


main()
