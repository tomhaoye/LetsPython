#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displaycount(self):
        print "Total Employee %d" % Employee.empCount

    def displayemployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"

"创建 Employee 类的第一个对象"
emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displaycount()
emp2.displayemployee()
print "Total Employee %d" % Employee.empCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
