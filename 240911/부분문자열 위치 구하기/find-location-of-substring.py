inp = input()
target = input()
idx = 0

for i in range(len(inp)):
    if(inp[i] == target[idx]):
        idx+=1
        if(idx == len(target)):
            print(i-idx+1)
            break
    else:
        idx=0
    if(i==len(inp)-1):
        print(-1)