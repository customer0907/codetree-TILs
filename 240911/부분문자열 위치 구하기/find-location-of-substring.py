import sys

inp = input()
target = input()
is_matched = False

for i in range(len(inp)):
    
    is_matched = True
    for j in range(len(target)):
        if(inp[i+j] != target[j]):
            is_matched = False

    if(is_matched == True):
        print(i)
        sys.exit(0)

print(-1)