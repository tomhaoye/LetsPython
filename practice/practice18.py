#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = 0
num = int(raw_input('input a single number:\n'))
n = int(raw_input('input the times:\n'))
for count in range(n):
    single = num
    s += num
    num = 10 * num + single

print s
