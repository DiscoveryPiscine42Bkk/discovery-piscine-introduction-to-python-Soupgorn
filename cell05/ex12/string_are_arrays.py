#!/usr/bin/env python3
import sys
args = sys.argv[1:]
if len(args) == 0 :
    print("none")
else :
    text = str(sys.argv[1:])
    z_count = text.count('z')
    print("z" * z_count)