x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

offset = 1000
_max = 2000
arr = [[0] * (_max+1) for _ in range(_max+1)]

i = 0
cnt = 0

for i in range(3):
    for j in range(x1[i]+offset,x2[i]+offset):
        for k in range(y1[i]+offset,y2[i]+offset):
            if i == 0:
                arr[j][k] = 1
            elif i == 1:
                arr[j][k] = 2
            else:
                arr[j][k] = 3


for n in range(_max+1):
    for m in range(_max+1):
        if arr[n][m] == 1 or arr[n][m] == 2:
            cnt+=1
    
print(cnt)
