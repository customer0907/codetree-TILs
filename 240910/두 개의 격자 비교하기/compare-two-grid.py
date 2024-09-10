import sys

n,m = map(int,sys.stdin.readline().split())
fst_lat = []
snd_lat = []

for i in range(n):
    fst_lat.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    snd_lat.append(list(map(int,sys.stdin.readline().split())))

new_lat = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if(fst_lat[i][j] == snd_lat[i][j]):
            new_lat[i][j] = 0
        else:
            new_lat[i][j] = 1

for i in range(n):
    for j in range(m):
            print(new_lat[i][j],end=" ")
    print()