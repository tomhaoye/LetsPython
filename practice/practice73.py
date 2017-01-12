#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(raw_input('input a number:'))
        ptr.append(num)

    ptr.reverse()
    print ptr
