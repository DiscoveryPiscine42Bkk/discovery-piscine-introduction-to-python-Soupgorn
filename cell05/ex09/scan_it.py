#!/usr/bin/env python3
import sys
import re
args = sys.argv[1:]

if len(args) != 2 :
    print(None)
else :
    keyword = sys.argv[1]
    text = sys.argv[2]
    a = re.findall(f"{keyword}",text)
    b = len(a)
    print(b)
