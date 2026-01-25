#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: StaticDecorator.py
# AUTHOR: Randall Nagy
# File: StaticDecorator.py
# Mission: How to statically decorate a class function.
#

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
