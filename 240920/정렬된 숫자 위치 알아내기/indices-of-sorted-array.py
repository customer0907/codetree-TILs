import sys

n = int(input())  
nums = list(map(int, sys.stdin.readline().split()))

new_nums = [(num,idx) for idx,num in enumerate(nums)]
new_nums.sort(key=lambda x:x[0])
ans_nums = [(number, index) for index, number in enumerate(new_nums)]
ans_nums.sort(key=lambda x:x[0][1])

for i in range(n):
    print(ans_nums[i][1]+1,end = ' ')