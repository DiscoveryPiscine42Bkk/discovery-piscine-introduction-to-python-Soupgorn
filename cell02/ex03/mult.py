#!/usr/bin/env python3
a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
axb = a*b
print(f"{a} x {b} = {axb}")
if axb == 0:
    print("The result is Postive and Negative")
elif axb > 0 :
    print("This result is Positive")
elif axb < 0 :
    print("This result is Negative")
