import sys

A,B = map(int,sys.stdin.readline().split())
N_list = sys.stdin.readline().strip()

result = []

def convertToDec(a):
    total = 0
    for i in N_list:
        total = total * a + int(i)
    
    return total

def convert(num, b):
    while(True):
        if(num<b):
            result.append(num)
            break

        remainder = num % b
        result.append(remainder)

        num //= b

decimal = convertToDec(A)
convert(decimal,B)

for i in result[::-1]:
    print(i,end='')