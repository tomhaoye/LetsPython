#!/usr/bin/python
# -*- coding: UTF-8 -*-


def foo():
    print 'foo'


def callfoo():
    print 'call'
    foo()

if __name__ == "__main__":
    callfoo()
