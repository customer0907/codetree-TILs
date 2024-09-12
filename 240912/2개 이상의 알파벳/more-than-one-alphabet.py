import sys

word = list(sys.stdin.readline())

after_word = set(word)

if(len(after_word)>=2):
    print("Yes")
else:
    print("No")