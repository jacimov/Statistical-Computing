"""
Generate a triangle of numbers for a given input.

For example, if the input is 3, it will print a 3x3 triangle.
"""

import sys

n = int(sys.argv[1])
print(f"Printing {n} lines:")
num = 1
for i in range(1, n + 1):
    print(*range(num, num + i))
    num += i
