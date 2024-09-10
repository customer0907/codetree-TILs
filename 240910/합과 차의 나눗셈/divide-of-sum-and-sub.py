import sys

a,b = map(int,sys.stdin.readline().split())

result = (a+b)/(a-b)

print(f"{result:.2f}")