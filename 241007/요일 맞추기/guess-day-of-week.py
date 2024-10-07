import sys

# 요일 맞추기
# m1, d1에서 m2, d2

Date = [0,31,28,31,30,31,30,31,31,30,31,30,31] # 13개의 배열
Day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int,sys.stdin.readline().split())

afterSum = 0
beforeSum = 0
total = 0

def predictDate(date, month):
    sum = 0
    for i in range(1,month):
        sum += Date[i]
    sum += date
    return sum

afterSum = predictDate(d2,m2)
beforeSum = predictDate(d1,m1)

total = afterSum - beforeSum # 날짜 수 차이

total %= 7
print(Day[total])