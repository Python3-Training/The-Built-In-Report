#!/usr/bin/env python3
# File: CompileEvalError.py
# Mission: Demonstrate bad 'eval' usage

try:
    a = 3
    print(f'before compile: a={a}')
    z = compile('a += 10', 'error.txt', 'eval')
    print(f'before eval: a={a}')
    eval(z)
    print(f'after eval: a={a}')
except:
    print("Yikes!")

