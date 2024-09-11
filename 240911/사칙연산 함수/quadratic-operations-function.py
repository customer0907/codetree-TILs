import sys

a,b,c = sys.stdin.readline().split()
a=int(a)
c=int(c)

def fourCal(fst_num, opt, snd_num):
    if(opt == '+'):
        print(f"{fst_num} + {snd_num} = {fst_num+snd_num}")
    elif(opt == '-'):
        print(f"{fst_num} - {snd_num} = {fst_num-snd_num}")
    elif(opt == '/'):
        print(f"{fst_num} / {snd_num} = {fst_num/snd_num:.0f}")
    elif(opt == '*'):
        print(f"{fst_num} * {snd_num} = {fst_num*snd_num}")
    else:
        print("False")

fourCal(a,b,c)