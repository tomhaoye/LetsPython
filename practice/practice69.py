#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    n = int(raw_input('input person amount:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    s = 1
    c = 1

    while s <= len(num):
        print 'c=', c, 's=', s
        if c == 3:
            del (num[s - 1])
            c = 1
        else:
            c += 1
            s += 1
        if s > len(num):
            s = 1
        print num
