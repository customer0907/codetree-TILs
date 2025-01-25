n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
_max = 0

for i in range(n):
    if i == 0:
        continue
        if t == 0:
            cnt+=1
            continue
    if arr[i] == arr[i-1]+1:
        cnt+=1
    else:
        _max = cnt+1
        cnt = 0

print(_max)