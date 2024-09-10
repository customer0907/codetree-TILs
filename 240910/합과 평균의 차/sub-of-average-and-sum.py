import sys

a,b,c = map(int,sys.stdin.readline().split())

sum = a+b+c
avg = (a+b+c)/3
result = sum-avg
print(sum)
print(f"{avg:.0f}")
print(f"{result:.0f}")