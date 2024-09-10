import sys

a,b = map(int,sys.stdin.readline().split())

arr = [0]*10

arr[0] = a
arr[1] = b

for i in range(2,10):
    arr[i] = arr[i-1]+2*arr[i-2]

for i in range(10):
    print(arr[i],end=' ')