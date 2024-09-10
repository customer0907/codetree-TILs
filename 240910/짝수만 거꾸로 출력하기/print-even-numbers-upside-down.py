import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))

for num in arr[::-1]:
    if(num%2 == 0):
        print(num,end=" ")