#!/usr/bin/env python3
# File: CompileEval.py
# Mission: Demonstrate 'eval' usage

z = compile('list("Nagy")', 'error.txt', 'eval')
a = eval(z)
print(a)

