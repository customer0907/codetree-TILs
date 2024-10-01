import sys

m1, d1, m2, d2 = map(int,sys.stdin.readline().split())

monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]

afterSum = 0
beforeSum = 0

for i in range(m2):
    afterSum += monthDays[i]

for i in range(m1):
    beforeSum += monthDays[i]

if(m1==m2):
    if(d1==d2):
        print(1)
    else:
        print(afterSum+d2-(beforeSum+d1))