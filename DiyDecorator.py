#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: DiyDecorator.py
# AUTHOR: Randall Nagy
# File: DiyDecorator.py
# Mission: How to decorate any function.
#

class Z:
    def __init__(self, func):
        print(type(func), func.__name__)
        self.a_func = func

    def __call__(self):
        print('Calling', self.a_func.__name__)
        results = self.a_func()
        print('Returning', results)
        return results
