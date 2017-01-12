#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    su = int(raw_input('input a sushu:'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % su == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print '%d can be divided by %d 9' % (sum, c9)
