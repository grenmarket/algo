import math
import sys

min1, min2, max = math.inf, math.inf, 0

n = int(input())
for _ in range(n):
    line = input()
    i = line.find('/')
    length = float(line[:i]) / float(line[i+1:].strip())
    if length < min1:
        min2 = min1
        min1 = length
    elif length < min2:
        min2 = length
    if length > max:
        max = length

if max >= min1 + min2:
    sys.stdout.write('NIE')
else:
    sys.stdout.write('TAK')