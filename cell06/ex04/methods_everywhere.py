#!/usr/bin/env python

import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    result = s
    while len(result) < 8:
        result += 'Z'
    print(result)

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
