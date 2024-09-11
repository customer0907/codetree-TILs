import sys

word = input()

for i in range(len(word)-1,-1,-1):
    if(i%2 != 0):
        print(word[i],end="")