#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: BltReport.py
# AUTHOR: Randall Nagy
# Mission: Keep track of cross-plat 'builtins.
#

# Rev: 1.1.0

import MkEvalFile

covered = ['False', 'None', 'True', 'bool',
           'type', 'int', 'eval', 'quit', 'exit',
           'input','print', 'copyright', 'credits',
           'license', 'vars', 'isinstance', 'issubclass',
           'hasattr','setattr', 'getattr', 'delattr',
           'object','enumerate', 'range', 'id', 'repr',
           'str', 'locals', 'globals', 'exec',
           'compile', 'staticmethod', 'callable',
           'classmethod','set', 'dict', 'hash',
           'frozenset']

def diff_eval(file_a, file_b):
    e13 = ''
    with open(file_a) as fh:
        x13 = eval(fh.read())
        print(type(x13), len(x13))
        e13 = set(x for x in x13 if x[0] != '_' and x.islower()) # beep
        print(e13)

    e10 = ''
    with open(file_b) as fh:
        x13 = eval(fh.read())
        print(type(x13), len(x13))
        e10 = set(x for x in x13 if x[0] != '_' and x.islower()) # boop

    ll = list(e13 - e10)
    ll.sort()
    return ll


def report(a_list, a_mod):
    for ss, item in enumerate(a_list,1):
        disp = chr(0x25b7)
        if item in covered:
            disp = chr(0x25b6)
        print(f"{disp:<2}{item:<13}", end='')
        if ss % a_mod == 0:
            print()
    print()


others = list()
common = ['False', 'None', 'True']
uncommon = []
sigma = dir(__builtins__)

import os.path
if not os.path.exists(MkEvalFile.get_fn()):
    MkEvalFile.create()

# sigma = sorted(dir(__builtins__), key=lambda a: len(a))
for ss, item in enumerate(sigma,1):
    if item.startswith('_'):
        uncommon.append(item)
        continue
    if not item.islower():
        others.append(item)
        continue
    common.append(item)

for the_list in [uncommon,2], [others,1], [common,4]:
    report(the_list[0],the_list[1])

sigma = 0
for a_list in uncommon, common, others:
    sigma += len(a_list)

version = MkEvalFile.get_version()
print(f"\nVersion {version}, \
Total = {sigma:>03} \n\
Common = {len(common)} \
Covered = {len(covered)} \
({int((len(covered)/len(common))*100)}%)")



