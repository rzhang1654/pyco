#!/usr/bin/env python
def func():
    pass

func.temp = 1

print(func.__dict__)

class TempClass:
    a = 1
    def temp_function(self):
        pass

print(TempClass.__dict__)
