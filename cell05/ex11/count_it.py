#!/usr/bin/env python3
import sys
import re
args = sys.argv[1:]
if len(args) == 1 :
    print("none")
else:
    print(f"parameters : {len(args)}")
    for param in args:
        print(f"{param} {len(param)}")