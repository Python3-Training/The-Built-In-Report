#!/usr/bin/env python3
# File: CompileSingle.py
# Mission: Demonstrate 'single' usage

a = 3
print(f'before compile: a={a}')
z = compile('a += 10', 'error.txt', 'single')
print(f'before eval: a={a}')
eval(z)
print(f'after eval: a={a}')

