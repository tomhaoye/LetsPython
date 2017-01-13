#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    fp = open('text.txt', 'w')
    s = raw_input('input string:')
    s = s.upper()
    fp.write(s)
    fp = open('text.txt', 'r')
    print fp.read()
    fp.close()
