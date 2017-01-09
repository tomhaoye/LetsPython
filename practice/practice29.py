#!/usr/bin/python
# -*- coding: UTF-8 -*-


def backward(s, l):
    if l == 0:
        return
    print s[l - 1]
    backward(s, l - 1)


x = raw_input("请输入一个数:\n")
print '%d 位数' % len(x)
backward(x, len(x))
