import sys

word = list(sys.stdin.readline())

def alphaOverTwo(_word):
    after_word = set(_word)
    if(len(after_word)>=2):
        print("Yes")
    else:
        print("No")

alphaOverTwo(word)