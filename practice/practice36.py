#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输出指定范围内的素数

# take input from stdinput
low = int(raw_input('input low:'))
up = int(raw_input('input up:'))

for num in range(low, up + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print num
