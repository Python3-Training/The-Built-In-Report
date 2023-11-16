#!/usr/bin/env python3
# File: ClassDecorator.py
# Mission: Decorating class methods.

class S:
    def __init__(self, msg='Default'):
        if msg: print(msg)

    @classmethod
    def foo(cls):
        return cls('classM')

    @staticmethod
    def __call__():
        return S('staticM')


# Exampled:
# --------
print('S()()')
S()()
print('S().foo()')
S().foo()
