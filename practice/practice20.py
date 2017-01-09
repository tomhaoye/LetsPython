#!/usr/bin/python
# -*- coding: UTF-8 -*-

h = 100.0
hn = h / 2
s = 0

n = int(raw_input('input times:\n'))

for i in range(1, n + 1):
    s += h
    h = hn
    hn /= 2

print 'total %f' % s
print '%d times high %f' % (n, hn)
