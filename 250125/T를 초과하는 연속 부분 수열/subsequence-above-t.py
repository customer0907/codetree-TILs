n, t = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
_max = 0

for i in range(n):
    if arr[i] > t:
        cnt+=1
    else:
        _max = cnt
        cnt = 0

print(_max)