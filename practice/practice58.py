#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    from Tkinter import *

    root = Tk()
    root.title('ractangle')
    canvas = Canvas(root, width=600, height=600, bg='yellow')
    x0 = 263
    y0 = 263
    x1 = 275
    y1 = 275
    canvas.pack()

    for i in range(20):
        canvas.create_rectangle(x0, y0, x1, y1)
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    mainloop()
