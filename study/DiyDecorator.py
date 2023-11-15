#!/usr/bin/env python3
# File: DiyDecorator.py
# Mission: How to decorate any function.

class Z:
    def __init__(self, func):
        print(type(func), func.__name__)
        self.a_func = func

    def __call__(self):
        print('Calling', self.a_func.__name__)
        results = self.a_func()
        print('Returning', results)
        return results
