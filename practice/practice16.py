#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))

    myBD = datetime.date(1993, 9, 1)
    print myBD.strftime('%d/%m/%Y')

    myBDND = myBD + datetime.timedelta(days=1)
    print myBDND.strftime('%d/%m/%Y')
