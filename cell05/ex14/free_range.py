#!/usr/bin/env python3
import sys
args = sys.argv[1:]

if  len(args) != 2  :
    print(None)
else :
    start = int(args[0])
    end = int(args[1])
    answer = list(range(start, end+1))
    print(answer)