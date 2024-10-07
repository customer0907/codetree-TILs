import sys

# 요일 맞추기
# m1, d1에서 m2, d2

Date = [0,31,29,31,30,31,30,31,31,30,31,30,31] # 13개의 배열
Day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = map(int,sys.stdin.readline().split())
inputDay = sys.stdin.readline().strip()

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

# 몫과 나머지
quotient = total//7
remainder = total%7 # 나머지의 인덱스가 inputDay보다 작은지 큰지 판단해서 포함여부 판단

cnt = quotient

if(remainder>=Day.index(inputDay)): # 만약 크거나 포함된다면 몫에 더하기
    cnt += 1    

print(cnt)