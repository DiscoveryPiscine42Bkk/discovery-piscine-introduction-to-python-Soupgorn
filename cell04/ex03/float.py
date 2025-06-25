#!/usr/bin/env python3
import sys
a = input("Give me a number: ")
try :
    b = int(a)
    print("This number is an integer")
except ValueError :
    try :
        b = float(a)
        print("This is a decimal number")
    except ValueError:
        print("That's not a valid number")
        SystemExit(1)

