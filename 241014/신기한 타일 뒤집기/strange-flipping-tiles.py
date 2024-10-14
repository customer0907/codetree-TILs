import sys

MAX_K = 100000
n = int(input())
arr = [0]*(2*MAX_K+1)
cnt_b = [0]*(2*MAX_K+1)
cnt_w = [0]*(2*MAX_K+1)
w,b = 0,0
cur = MAX_K

for _ in range(n):
    x, direction = tuple(sys.stdin.readline().split())
    x = int(x)
    
    if direction == 'L':
        while x>0:
            arr[cur] = 1 # 흰색 색칠
            x-=1

            if x:
                cur-=1
    else:
        while x>0:
            arr[cur] = 2 # 검은색 색칠
            x-=1

            if x:
                cur+=1
    
for i in range(2*MAX_K+1):
    if arr[i] == 1:
        w+=1
    elif arr[i] ==2:
        b+=1

print(w,b,end=' ')