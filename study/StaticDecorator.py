#!/usr/bin/env python3
# File: StaticDecorator.py
# Mission: How to statically decorate a class function.

class S:
    def __init__(self): ...

    @staticmethod
    def foo():
        print('Spam! =)')

    @staticmethod
    def __call__():
        results = 5
        print('Returning', results)
        return results
