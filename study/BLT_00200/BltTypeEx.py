#!/usr/bin/env python3
# File: BltTypeEx.py
# Mission: Demonstrate extended type() usage      
class zclass:
    def __init__(self, **kwargs):
        self.times = 1000
        print(f'Created zclass {kwargs}')

normal = zclass(times=3000)
print('1',vars(normal))

other = type('zclass', tuple(), dict(times=9000))
print('2',vars(other))

