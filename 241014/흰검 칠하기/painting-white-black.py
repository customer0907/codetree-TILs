import sys

MAX_K = 100000
n = int(input())

arr = [0] * (2*MAX_K+1)
cnt_b = [0] * (2*MAX_K+1)
cnt_w = [0] * (2*MAX_K+1)
b,w,g = 0, 0, 0
cur = MAX_K

for _ in range(n):
    x, direction = tuple(sys.stdin.readline().split())
    x = int(x)

    if direction == 'L':
        for _ in range(x):
            cnt_w[cur] +=1 # cur idx에 흰색 색칠
            arr[cur] = 1 # 1은 흰색
            cur -=1
        cur+=1
    else:
        for _ in range(x):
            cnt_b[cur] +=1 # cur idx에 검은색 색칠
            arr[cur] = 2 # 2는 검은색
            cur +=1
        cur-=1
        
for i in range(2*MAX_K+1):
    if cnt_b[i] >=2 and cnt_w[i] >=2:
        g+=1
    elif arr[i] == 1:
        w+=1
    elif arr[i] == 2:
        b+=1

print(w,b,g)


# true, false
# class 만들어서, white, black counting & state
#