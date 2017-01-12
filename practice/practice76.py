#!/usr/bin/python
# -*- coding: UTF-8 -*-


def ou(n):
    s = 0.0
    if n < 2:
        return 0
    else:
        for j in range(n, 0, -2):
            s += (1.0 / j)
            print j
        return s


def ji(n):
    s = 0.0
    if n < 1:
        return 0
    else:
        for i in range(n, 0, -2):
            s += (1.0 / i)
            print i
        return s


if __name__ == '__main__':
    n = int(raw_input('input a number:'))
    if n % 2 == 0:
        print ou(n)
    else:
        print ji(n)
