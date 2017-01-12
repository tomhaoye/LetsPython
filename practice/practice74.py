#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    arr1 = [1, 4, 5, 6, 7, 3]
    arr2 = [11, 2, 43, 22, 15, 9]
    arr1.extend(arr2)
    arr1.sort()
    print arr1
