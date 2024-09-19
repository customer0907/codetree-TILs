import sys

n = int(input())

arr = list(map(int,sys.stdin.readline().split()))

def gcd(x,y):
    while(y):
        x,y = y,x%y
    return x

def lcm(a,b):
    return a*b // gcd(a,b)

def min_mul(num, arr):
    if(num==0):
        return arr[0]
    return lcm(min_mul(num-1, arr),arr[num])
print(min_mul(n-1, arr))