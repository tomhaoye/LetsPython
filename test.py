#!/usr/bin/python
# -*- coding: UTF-8 -*-

if 1:
    print 'true'
else:
    print 'false'

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

print 'aa'
print 'aaa'

'''
-------------------------------
'''

str = 'Hello World!'

print str  # 输出完整字符串
print str[0]  # 输出字符串中的第一个字符
print str[2:5]  # 输出字符串中第三个至第五个之间的字符串
print str[2:]  # 输出从第三个字符开始的字符串
print str * 2  # 输出字符串两次
print str + "TEST"  # 输出连接的字符串

'''
-------------------------------
'''

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表

'''
-------------------------------
'''

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

'''
-------------------------------
'''

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值

'''
-------------------------------
'''

a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if "H" in a:
    print "H 在变量 a 中"
else:
    print "H 不在变量 a 中"

if "M" not in a:
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"

print r'\n'
print R'\n'

'''
-------------------------------
'''

print "My name is %s and weight is %d kg!" % ('Zara', 21)

'''
-------------------------------
'''

import time  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks

localtime = time.localtime(time.time())
print "本地时间为 :", localtime

localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

'''
-------------------------------
'''

import calendar

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal

'''
-------------------------------
'''

# 导入内置math模块
import math

content = dir(math)

print content

'''
-------------------------------
'''

input_str = raw_input("请输入：")
print "你输入的内容是: ", input_str

'''
-------------------------------
'''


class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args
