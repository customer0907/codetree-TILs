import sys

n,m = map(int,sys.stdin.readline().split())
point = []

for i in range(m):
    point.append(list(map(int,sys.stdin.readline().split())))

arr = [[0 for _ in range(n)] for _ in range(n)]

for x,y in point:
    arr[x-1][y-1] = x*y

for row in arr:
    print(" ".join(map(str,row)))