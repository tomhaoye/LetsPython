#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = 0
t = 1
for i in range(1, 21):
    t *= i
    s += t

print s
