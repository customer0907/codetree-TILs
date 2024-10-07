import sys

N = int(input())

is_overlap = [0] * 100

for i in range(N):
    x1, x2 = map(int,input().split())
    for j in range(x1,x2+1):
        is_overlap[j] += 1

print(max(is_overlap))