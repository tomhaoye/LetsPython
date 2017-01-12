#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    mima = raw_input('input you code:')
    encode = []
    for i in range(len(mima)):
        encode.append((int(mima[i]) + 5) % 10)
    encode.reverse()
    print encode
