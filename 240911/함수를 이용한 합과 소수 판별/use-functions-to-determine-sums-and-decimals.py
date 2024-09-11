import sys

a, b = sys.stdin.readline().split()

a = int(a)
b = int(b)

def sum_and_prime(_a, _b):
    cnt = 0
    for i in range(_a,_b):
        total = 0
        is_prime = True
        for num in range(2,i):
            if(i%num == 0):
                is_prime = False
            else:
                continue
        if is_prime:
            i = str(i)
            for digit in i:
                total += int(digit)    
            if(total%2==0):
                cnt+=1
    print(cnt)

sum_and_prime(a,b+1)