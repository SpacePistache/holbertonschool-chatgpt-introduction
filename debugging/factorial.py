#!/usr/bin/python3
import sys
import math

if len(sys.argv) != 2:
    print("Usage: ./script_name.py <non-negative integer>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        sys.exit(1)
    print(f"{math.factorial(n)}")
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)
