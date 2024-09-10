import sys
import math

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))

# 10C2 의 경우의 수
min = 100

for i in range(0,n):
    for j in range(i+1,n):
        if abs(arr[i]-arr[j])<min:
            min = abs(arr[i]-arr[j])

print(min)