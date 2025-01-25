n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
_max = 0

for i in range(n):
    if arr[i] > t:
        if i == 0:
            _max = 1
            continue
        elif arr[i] == arr[i-1]+1:
            cnt+=1
    else:
        _max = cnt+1
        cnt = 0

print(_max)