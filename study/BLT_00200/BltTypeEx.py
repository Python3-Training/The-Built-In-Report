#!/usr/bin/env python3
# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.1.0
# NOTES: tbd.
# DATE: 2026-01-25 10:56:41
# FILE: BltTypeEx.py
# AUTHOR: tbd.
# File: BltTypeEx.py
# Mission: Demonstrate extended type() usage
#
class zclass:
    def __init__(self, **kwargs):
        self.times = 1000
        print(f'Created zclass {kwargs}')

normal = zclass(times=3000)
print('1',vars(normal))

other = type('zclass', tuple(), dict(times=9000))
print('2',vars(other))

