#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in range(100, 1000):
    f = i / 100
    s = (i / 10) % 10
    t = i % 10
    if f ** 3 + s ** 3 + t ** 3 == i:
        print i
