import sys

word, n = sys.stdin.readline().split()
n = int(n)

arr = []

for i in range(n):
    arr.append(sys.stdin.readline().strip())

for idx in arr:
    if(idx=='1'):
        word = word[1:]+word[0]
        print(word)
    elif(idx=='2'):
        word = word[-1]+word[:-1]
        print(word)
    else:
        word = word[::-1]
        print(word)