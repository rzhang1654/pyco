#!/usr/bin/env python
class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    @classmethod
    def from_csv(cls, name_str):
        first_name, last_name = map(str, name_str.split(','))
        student = cls(first_name, last_name)
        return student

scott = Student.from_string('Scott Robinson')
print "my name is : %s %s" % (scott.first_name, scott.last_name)
scott1 = Student.from_csv('Scott,Robinson')
print "my name is : %s %s" % (scott1.first_name, scott1.last_name)
