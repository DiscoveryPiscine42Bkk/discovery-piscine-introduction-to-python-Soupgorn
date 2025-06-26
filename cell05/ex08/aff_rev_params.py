#!/usr/bin/env python3
import sys
args = sys.argv[1:]

if len(args) < 2 :
    print(None)
else :
    rev_args = args[::-1]
    print(rev_args)