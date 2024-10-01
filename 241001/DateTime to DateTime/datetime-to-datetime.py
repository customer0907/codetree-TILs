import sys

a,b,c = map(int,sys.stdin.readline().split())

def dateTimeGap(d,h,m):
    minute = (d-11)*24*60+h*60+m

    minute -= 11*60+11
    if(minute<0):
        print(1)

    return minute

total = dateTimeGap(a,b,c)
print(total)

# 11월 12일 9시 10분이면
# 24시간 + 9시 + 10이고
# 


# 11일 00시 00분 기준으로 해서, 마지막에 11시11분을 더해주는 걸로 (11*60+11)