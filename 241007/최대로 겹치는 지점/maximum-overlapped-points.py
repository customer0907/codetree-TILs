import sys

N = sys.stdin.readline().split()
N = int(N)

arr = []
is_overlap = [0] * 100

for i in range(N):
    x1, x2 = map(int,sys.stdin.readline().split())
    arr.append((x1,x2))

for x1,x2 in arr:
    for j in range(x1,x2+1):
        is_overlap[j] +=1
        
print(max(is_overlap))