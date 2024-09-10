import sys

fst_man = sys.stdin.readline().split()
snd_man = sys.stdin.readline().split()

if((int(fst_man[0])>=19 and fst_man[1] == 'M') or (int(snd_man[0])>=19 and snd_man[1] == 'M')):
    print("1")
else:
    print("0")