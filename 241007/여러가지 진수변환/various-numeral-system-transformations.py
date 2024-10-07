import sys

N, B = map(int,sys.stdin.readline().split())

result = []

def convert(num, b):
    while(True):
        if(num<b):
            result.append(num)
            break

        remainder = num % b
        result.append(remainder)

        num //= b

convert(N,B)

for i in result[::-1]:
    print(i,end='')