#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = int(raw_input('净利润:'))
arr = [0, 100000, 200000, 400000, 600000, 1000000]
rat = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
r = 0
for index in range(5, -1, -1):
    if i > arr[index]:
        r += (i - arr[index]) * rat[index]
        i = arr[index]
print r
