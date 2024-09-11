import sys

input_str = input()
target_str = input()
cnt=0

for i in range(len(input_str)):
    for j in range(len(target_str)):
        if(input_str[i+j] == target_str[j]):
            if(j==len(target_str)-1):
                cnt+=1
        else:
            break

print(cnt)