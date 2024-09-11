import sys

n = int(input())
total = 0

arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip())

for item in arr:
    total += int(item)

total = str(total)
print(total[1:]+total[0])