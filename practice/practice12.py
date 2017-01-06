#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math

h = 0
leap = 1
for i in range(101, 201):
    k = int(math.sqrt(i))
    for m in range(2, k + 1):
        if i % m == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % i
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'total : %d' % h
