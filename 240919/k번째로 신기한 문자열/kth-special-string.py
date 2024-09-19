import sys

n, k, word = sys.stdin.readline().split()

n = int(n)
k = int(k)
words = []
new_arr = []

for i in range(n):
    words.append(sys.stdin.readline().strip())

for i in range(n):
    is_matched = True
    for j in range(len(word)):
        if words[i][j] == word[j]:
            continue
        else:
            is_matched = False
            break
    if is_matched:
        new_arr.append(words[i])

new_arr.sort()
print(new_arr[k-1])