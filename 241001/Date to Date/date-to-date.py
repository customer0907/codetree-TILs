import sys

m1, d1, m2, d2 = map(int,sys.stdin.readline().split())

monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31] # size : 13

afterSum = 0
beforeSum = 0

for i in range(1,m2): # 12월이면, 11인덱스까지.
    afterSum += monthDays[i]

for i in range(1,m1):
    beforeSum += monthDays[i]

print((afterSum+d2)-(beforeSum+d1)+1)