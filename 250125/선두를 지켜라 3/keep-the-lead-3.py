N, M = map(int, input().split())

a_move = []
b_move = []

for i in range(N):
    x, y = map(int,input().split())
    for j in range(y):
        a_move.append(x)

for i in range(M):
    x, y = map(int,input().split())
    for j in range(y):
        b_move.append(x)

dist_A = 0
dist_B = 0
state = []
state.append(0)
cnt = 0

for i in range(len(a_move)):
    dist_A += a_move[i]
    dist_B += b_move[i]

    if dist_A > dist_B:
        if state[-1] == 1 or state[-1] == 2: # B가 명예의전당이었으면
            cnt+=1
        state.append(0) # A 명예의전당
    elif dist_B > dist_A:
        if state[-1] == 0 or state[-1] == 2: # A가 명예의전당이었으면
            cnt+=1
        state.append(1) # B 명예의전당
    else:
        if state[-1] == 0 or state[-1] == 1:
            cnt+=1
        state.append(2)

print(cnt)
# Write your code here!