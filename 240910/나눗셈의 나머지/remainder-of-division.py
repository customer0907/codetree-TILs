import sys

a,b = map(int,sys.stdin.readline().split())

arr = [0]*1000
total = 0

while(a !=0):
    remainder = a%b
    arr[remainder] +=1
    a = a//b

for i in range(1000):
    if(arr[i]!=0):
        total+=arr[i]**2

print(total)