#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    c = 0
    n = raw_input('input a  octal number:')
    for i in range(len(n)):
        c = 8 * c + ord(n[i]) - ord('0')
    print c
