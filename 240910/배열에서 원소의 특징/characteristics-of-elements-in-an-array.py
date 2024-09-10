import sys

data = list(map(int,sys.stdin.readline().split()))

for i in data:
    if(i%3==0):
        print(data[data.index(i)-1])
        break