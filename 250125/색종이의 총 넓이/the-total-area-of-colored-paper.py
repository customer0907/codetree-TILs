n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

offset = 100
_max = 200
cnt = 0

arr = [[0] * (_max) for _ in range(_max)]

for i in range(n):
    for j in range(x[i]+offset, x[i]+offset+8):
        for k in range(y[i]+offset, y[i]+offset+8):
            arr[j][k] = 1

for i in range(_max):
    for j in range(_max):
        if arr[i][j] == 1:
            cnt+=1

print(cnt)
