#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if not args:
    print("none")
for param in args:
    if not param.endswith("ism"):
        print(param + "ism")