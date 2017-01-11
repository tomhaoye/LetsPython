#!/usr/bin/python
# -*- coding: UTF-8 -*-

TRUE = 1
FALSE = 0


def SQ(x):
    return x * x


print 'little than 50 then stop'
again = 1
while again:
    num = int(raw_input('input a num:'))
    print 'result = %d' % (SQ(num))
    if num > 50:
        again = TRUE
    else:
        again = FALSE
