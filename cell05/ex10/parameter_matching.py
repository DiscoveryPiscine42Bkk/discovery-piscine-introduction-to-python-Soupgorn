#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 2 :
    print(None)

args = sys.argv[1]
answer = input("What was the parameter? : ")

if args == answer:
    print("Good job!")
else :
    print("Nope, sorry...")