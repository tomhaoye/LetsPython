#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sys import stdout

n = int(raw_input('input lines:\n'))

for i in range(n):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print
