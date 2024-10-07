import sys

N = int(sys.stdin.readline())

is_visited = [0] * 2001
cur_idx = 1000


for _ in range(N):
    x, dir = sys.stdin.readline().split()
    x = int(x)

    if(dir == "R"):
        for i in range(cur_idx-x, cur_idx):
            is_visited[i] += 1
        cur_idx = cur_idx-x
    else:
        for i in range(cur_idx,cur_idx+x):
            is_visited[i] += 1
        cur_idx = cur_idx+x

cnt=0

for i in is_visited:
    if(i>=2):
        cnt+=1

print(cnt)