#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    import time

    start = time.time()
    for i in range(3000):
        print 1
    end = time.time()

    print end - start
