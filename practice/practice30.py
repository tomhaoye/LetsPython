#!/usr/bin/python
# -*- coding: UTF-8 -*-

x = raw_input('input a number:\n')
flag = True

for i in range(len(x)):
    if x[i] != x[-i - 1]:
        flag = False
        break

if flag:
    print '%d yes' % int(x)
else:
    print '%d no' % int(x)
