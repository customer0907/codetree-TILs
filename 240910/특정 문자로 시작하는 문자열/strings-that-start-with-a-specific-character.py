import sys

arr = []
cnt = 0
total = 0
avg = 0

n = int(input())
for i in range(n):
    arr.append(sys.stdin.readline().strip())
alp = input()

for i in range(n):
    if(arr[i][0] == alp):
        cnt+=1
        total+=len(arr[i])

avg = round(total/3,2)

print(f"{cnt} {avg:.2f}")