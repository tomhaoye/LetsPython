#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from Tkinter import *

    canvas = Canvas(width=600, height=600, bg='blue')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    for i in range(20):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red')
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='green')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()
