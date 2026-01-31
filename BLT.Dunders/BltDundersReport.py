#!/usr/bin/env python3
# MISSION: Tag & track the officially reviewed / covered items.
# STATUS: Research
# VERSION: 0.0.1
# NOTES: Getting started.
# DATE: 2026-01-31 06:47:28
# FILE: BltDundersReport.py
# AUTHOR: Randall Nagy

from get_dunders import get_dunders

covered = [ # Nada outside of the training here, yet.
    ]

def report(a_mod = 3):
    items = get_dunders()
    for ss, item in enumerate(items,1):
        disp = chr(0x25b7)
        if item in covered:
            disp = chr(0x25b6)
        print(f"{disp:<2}{item:<22}", end='')
        if ss % a_mod == 0:
            print()
    print()
    print(f"There are {len(items)} 'dunders listed.")

report()



