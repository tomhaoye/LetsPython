#!/usr/bin/python
# -*- coding: UTF-8 -*-


def gui(n):
    if n >= 1:
        s = n * gui(n - 1)
    else:
        s = 1
    return s


print gui(5)
