import sys

a,b = input().split()
str1 = ''
str2 = ''
idx1 = 0
idx2 = 0

for item in a:
    if(item > '9' or item < '0'):
        break
    else:
        str1+=item

for item in b:
    if(item > '9' or item < '0'):
        break
    else:
        str2+=item

print(int(str1)+int(str2))