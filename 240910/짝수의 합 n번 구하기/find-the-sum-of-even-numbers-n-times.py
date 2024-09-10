import sys

n = int(input())
data = list(map(int,sys.stdin.readline().split()) for _ in range(n))

for i in range(n):
    a, b = data[i]
    total = 0
    for num in range(a,b+1):
        if(num%2 == 0):
            total += num
    print(total)