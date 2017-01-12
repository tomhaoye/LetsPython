#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    for i in range(7):
        n = int(raw_input('input a number:'))
        while n > 50 or n < 1:
            n = int(raw_input('input a number:'))
        print n * '*'
