n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
_max = 0

for i in range(n):
    if arr[i] > t:
        cnt+=1
        _max = max(_max,cnt)
    else:
        cnt = 0

print(_max)