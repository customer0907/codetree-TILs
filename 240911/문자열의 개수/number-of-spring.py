import sys

arr = []

while(1):
    word = sys.stdin.readline().strip()
    if(word=='0'):
        break
    else:
        arr.append(word)

print(len(arr))

for idx in range(len(arr)):
    if(idx%2==0):
        print(arr[idx])