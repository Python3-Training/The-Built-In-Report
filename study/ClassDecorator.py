#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: ClassDecorator.py
# AUTHOR: Randall Nagy
# File: ClassDecorator.py
# Mission: Decorating class methods.
#

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
