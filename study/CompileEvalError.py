#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: CompileEvalError.py
# AUTHOR: Randall Nagy
# File: CompileEvalError.py
# Mission: Demonstrate bad 'eval' usage
#

try:
    a = 3
    print(f'before compile: a={a}')
    z = compile('a += 10', 'error.txt', 'eval')
    print(f'before eval: a={a}')
    eval(z)
    print(f'after eval: a={a}')
except:
    print("Yikes!")

