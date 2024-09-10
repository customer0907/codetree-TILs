import sys

a,b = map(int,sys.stdin.readline().split())

a += 8
b *= 3

print(a)
print(b)
print(a*b)