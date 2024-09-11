import sys

word, n = sys.stdin.readline().split()
n = int(n)
arr = []

for i in range(n):
    arr.append(list(sys.stdin.readline().split()))

word_res = list(word)

for row in arr:
    if(row[0]=='1'):
        word_res[int(row[1])-1], word_res[int(row[2])-1] = word_res[int(row[2])-1], word_res[int(row[1])-1]
        print(''.join(word_res))
    elif(row[0]=='2'):
        for i in range(len(word_res)):
            if(word_res[i]==row[1]):
                word_res[i]=row[2]
        print(''.join(word_res))
    else:
        break