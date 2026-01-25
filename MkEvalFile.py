#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: MkEvalFile.py
# AUTHOR: Randall Nagy
#

'''Mission: Define & create the .eval file
anywhere Python 3 is sold.'''

def get_version():
    ''' Concoct the version / file name identifier '''
    import sys
    version = sys.version.split(' ')[0] + '_'
    version += sys.platform.upper()
    return version

def get_fn():
    ''' Get the file name for our version. '''
    return get_version() + '.eval'

def create():
    ''' Create / overwrite an eval file. '''
    a_file = get_fn()
    sigma = dir(__builtins__)
    with open(a_file, 'w') as fh:
        print(sigma, file=fh)
    return a_file

if __name__ == '__main__':
    print("Created", create())
    
