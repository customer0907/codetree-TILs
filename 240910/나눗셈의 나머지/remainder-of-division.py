import sys

a,b = map(int,sys.stdin.readline().split())

arr = [0]*b
total = 0

while a > 1:
    remainder = a%b
    arr[remainder] +=1
    a = a//b

for count in arr:
    total += count**2

print(total)