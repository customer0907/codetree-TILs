import sys

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

i,j = n-1, n-1
cnt = 1

while(arr[n-1][0] != n**2 and arr[0][0] != n**2 and j>=0):
    if(j%2 != 0): # 홀수
        while(i>=0):
            arr[i][j] = cnt
            cnt+=1
            i-=1
        i=0
    else: # 짝수
        while(i<=n-1): 
            arr[i][j] = cnt
            cnt+=1
            i+=1
        i=n-1
    j-=1

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()