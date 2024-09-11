import sys

inp = input()
target = input()
is_matched = False

for i in range(len(inp)):
    for j in range(len(target)):
        if(inp[i+j] == target[j]):
            is_matched = True
        else:
            is_matched = False
            break
    if(is_matched == True):
        print(i)
        sys.exit(0)

print(-1)