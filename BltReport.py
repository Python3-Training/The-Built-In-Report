#!/usr/bin/env python3
# Mission: Keep track of cross-plat 'builtins.

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
