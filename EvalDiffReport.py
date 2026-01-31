#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: EvalDiffReport.py
# AUTHOR: Randall Nagy
# Mission: Show what has changed between .eval files.
#

def report(a_list, a_mod):
    for ss, item in enumerate(a_list,1):
        disp = chr(0x25b7)
        if item in covered:
            disp = chr(0x25b6)
        print(f"{disp:<2}{item:<13}", end='')
        if ss % a_mod == 0:
            print()
    print()


import os
items = {}
for item in os.listdir():
    if not item.endswith('.eval'):
        continue
    with open(item) as fh:
        items[item] = set(eval(fh.read()))

gotcha = []
for ka in items:
    for kb in items:
        if ka is kb:
            continue
        print(ka, kb, sep = ' ~v~ ')
        difa = items[ka] - items[kb]
        difb = items[kb] - items[ka]
        if difa == difb:
            gotcha.append(difa)
            print('\t',difa)
        else:
            a_union = difa.union(difb)
            if a_union in gotcha:
                print('\tmeh... ')
            gotcha.append(a_union)
            for ss, line in enumerate(sorted(a_union), 1):
                print(f'\t{ss}.) {line}')
        print()
        
