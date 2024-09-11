import sys

input_str = input()
target_str = input()
input_str = list(input_str)

i=0

while(i<len(input_str)):
    if(i+len(target_str)-1>=len(input_str)):
        break
    for j in range(len(target_str)):
        if(input_str[i+j] == target_str[j]):
            if(j==len(target_str)-1):
                print(i,j)
                input_str = input_str[:i]+input_str[i+j+1:]
                i=0
                break
        else:
            i+=1
            break

print(input_str)