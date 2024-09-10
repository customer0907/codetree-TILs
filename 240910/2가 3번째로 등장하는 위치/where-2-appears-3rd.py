import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))

count = 0
idx = 0

for i in range(n):
    if(arr[i]==2):
        count+=1
    if(count==3):
        print(i+1)
        break