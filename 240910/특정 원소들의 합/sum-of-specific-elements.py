import sys

arr = []
for i in range(4):
    arr.append(list(map(int,sys.stdin.readline().split())))
total = 0

for i in range(0,4):
    for j in range(0,i+1):
        total += arr[i][j]

print(total)