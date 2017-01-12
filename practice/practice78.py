#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    person = {"li": 18, "qiu": 23, "chen": 23, "da": 24, "kun": 25}
    maxp = "li"
    for key in person.keys():
        if person[maxp] < person[key]:
            maxp = key

    print maxp
