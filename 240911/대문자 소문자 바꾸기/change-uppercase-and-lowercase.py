words = list(input())

for i in range(len(words)):
    if 'A' <= words[i] and words[i] <= 'Z':
        words[i] = chr(ord(words[i])-ord('A')+ord('a'))
    else:
        words[i] = chr(ord(words[i])-ord('a')+ord('A'))

print(''.join(words))