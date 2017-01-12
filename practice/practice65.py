#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
from Tkinter import *


class PTS:
    def __init__(self):
        self.x = 0
        self.y = 0


points = []


def LineToDemo():
    screenx = 400
    screeny = 400
    canvas = Canvas(width=screenx, height=screeny, bg='white')

    AspectRadio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    yc = h / 2
    xc = w / 2
    radius = (h - 30) / (AspectRadio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xc + int(math.cos(rads) * radius)
        p.y = yc = int(math.sin(rads) * radius * AspectRadio)
        angle += step
        points.append(p)
    canvas.create_oval(xc - radius, yc - radius, xc + radius, yc + radius)
    for i in range(MAXPTS):
        for j in range(i, MAXPTS):
            canvas.create_line(points[i].x, points[i].y, points[j].x, points[j].y)

    canvas.pack()
    mainloop()


if __name__ == '__main__':
    LineToDemo()
