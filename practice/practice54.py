#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = int(raw_input('input a num:'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print '%o\t%o' % (a, d)