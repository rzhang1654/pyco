#!/usr/bin/env python
class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1

print Student.is_full_name('Scott Robinson')   # True
print Student.is_full_name('Scott')
