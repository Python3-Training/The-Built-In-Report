#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: CompileEval.py
# AUTHOR: Randall Nagy
# File: CompileEval.py
# Mission: Demonstrate 'eval' usage
#

z = compile('list("Nagy")', 'error.txt', 'eval')
a = eval(z)
print(a)

