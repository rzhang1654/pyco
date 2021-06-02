#!/usr/bin/env python
import functools

def uppercase_decorator(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    "This will say hi"
    return 'hello there'

print(say_hi())
print(say_hi.__name__)
print(say_hi.__doc__)
