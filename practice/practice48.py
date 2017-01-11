#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    i = int(raw_input('input a num:'))
    j = int(raw_input('input a num:'))
    if i > j:
        print '%d 大于 %d' % (i, j)
    elif i == j:
        print '%d 等于 %d' % (i, j)
    elif i < j:
        print '%d 小于 %d' % (i, j)
    else:
        print '未知'
