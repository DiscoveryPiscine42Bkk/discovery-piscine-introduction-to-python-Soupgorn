#!/usr/bin/env python3
a = [2, 8, 9, 48, 8, 22, -12, 2]
newlist = []
for x in a:
    if x>5 :
        newlist.append(x+2)
print(a)
print(set(newlist))