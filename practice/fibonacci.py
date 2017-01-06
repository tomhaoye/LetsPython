#!/usr/bin/python
# -*- coding: UTF-8 -*-


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print fib(10)


def rec_fib(n):
    if n == 1 or n == 2:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)


print rec_fib(10)


def th_fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return fibs


print th_fib(10)
