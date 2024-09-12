import sys

n, m = tuple(map(int,sys.stdin.readline().split()))
A = list(map(int,sys.stdin.readline().split()))

num_cp = []

for i in range(m):
    num_cp.append(list(map(int,sys.stdin.readline().split())))

def sum_seq():
    for i in range(m):
        total = 0
        for idx in range(num_cp[i][0]-1,num_cp[i][1]):
            total += A[idx]
        print(total)

sum_seq()