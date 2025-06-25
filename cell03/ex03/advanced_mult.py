#!/usr/bin/env python3
i = 0
while i <= 10:
    j = 0
    a = f"Table de {i}:"
    while j <= 10:
        a += f" {i * j}"
        j += 1
    print(a)
    i += 1
