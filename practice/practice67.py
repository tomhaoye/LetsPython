#!/usr/bin/python
# -*- coding: UTF-8 -*-


def inp(numbers):
    for i in range(9):
        numbers.append(int(raw_input('input a number:')))
    numbers.append(int(raw_input('input a number:')))


p = 0


def max_min(array):
    max = min = 0
    for i in range(1, len(array) - 1):
        p = i
        if array[p] > array[max]:
            max = p
        elif array[p] < array[min]:
            min = p
    k = max
    l = min
    array[0], array[l] = array[l], array[0]
    array[9], array[k] = array[k], array[9]


def output(numbers):
    for i in range(len(numbers)):
        print numbers[i]


if __name__ == '__main__':
    array = []
    inp(array)
    max_min(array)
    output(array)
