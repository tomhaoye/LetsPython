#!/usr/bin/python
# -*- coding: UTF-8 -*-


def backward(s, l):
    if l == 0:
        return
    print s[l - 1]
    backward(s, l - 1)


st = raw_input('input a string:\n')
le = len(st)
backward(st, le)
