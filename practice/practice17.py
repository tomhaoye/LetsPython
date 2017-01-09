#!/usr/bin/python
# -*- coding: UTF-8 -*-

import string

s = raw_input('input a line:\n')
letters = 0
space = 0
number = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        number += 1
    else:
        others += 1

print 'letters: %d, space: %d, number: %d, others; %d' % (letters, space, number, others)
