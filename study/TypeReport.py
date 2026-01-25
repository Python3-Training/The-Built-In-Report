#!/usr/bin/env python3
# MISSION: Manage Built-in Data Collection & Reporting.
# STATUS: Research
# VERSION: 1.1.0
# NOTES: See https://github.com/Python3-Training/The-Built-In-Report for more informat.
# DATE: 2026-01-25 10:56:41
# FILE: TypeReport.py
# AUTHOR: Randall Nagy
# File: TypeReport.py
# Mission: Share dynamic type reporters.
#

import enum

class View(enum.Enum):
    PUBLIC  = 1
    PRIVATE = 0
    ALL     = 9

class Rpt:
    @staticmethod
    def get_public(a_type)->set:
        if not isinstance(a_type, type):
            return {}
        return {s for s in dir(a_type) if s[0] != '_'}

    @staticmethod
    def get_private(a_type)->set:
        if not isinstance(a_type, type):
            return {}
        return {s for s in dir(a_type) if s[0] == '_'}

    @staticmethod
    def get_set(a_type)->set:
        if not isinstance(a_type, type):
            return {}
        return {*dir(a_type)}

    @staticmethod
    def resolve(a_type, view)->set:
        if view is View.PUBLIC:
            return Rpt.get_public(a_type)
        elif view is View.PRIVATE:
            return Rpt.get_private(a_type)
        else:
            return Rpt.get_set(a_type)
        return False # Yes - I know. ;-)

    @staticmethod
    def reporter(lines):
        if not lines:
            return False
        zMax = len(max(lines, key=lambda a: len(a))) + 4
        zCols = int(80 / zMax)
        for ss, line in enumerate(sorted(lines),1):
            print(f'{ss:>02} {line:<{zMax-3}}', end='')
            if ss % zCols == 0:
                print()
        print('\n')
        return True

    @staticmethod
    def common_report(a_type, b_type, view=View.PUBLIC)->bool:
        a = Rpt.resolve(a_type, view)
        b = Rpt.resolve(b_type, view)
        if not a or not b:
            return False
        return Rpt.reporter(sorted(a.intersection(b)))

    @staticmethod
    def type_report(a_type, view=View.PUBLIC)->bool:
        return Rpt.reporter(Rpt.resolve(a_type, view))
