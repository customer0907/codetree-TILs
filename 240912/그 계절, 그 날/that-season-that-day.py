import sys

y,m,d = [int(x) for x in sys.stdin.readline().split()]

def leap_year(year):
    is_leap = False
    if(year%4 ==0):
        is_leap = True
        if(year%100 ==0):
            is_leap = False
            if(year%400 == 0):
                is_leap = True
    else:
        is_leap = False
    return is_leap

def print_season(month):
    if(month >=3 and month <=5):
        print("Spring")
    elif(month >=6 and month <=8):
        print("Summer")
    elif(month >=9 and month <=11):
        print("Fall")
    else:
        print("Winter")

if(m == 2 or m == 4 or m == 6 or m == 9 or m == 11):
    if(m==2 and d == 29):
        if leap_year(y): # 윤년인 경우
            print_season(m)
            sys.exit(0)
        else: # 윤년이 아닌 경우
            print("-1")
            sys.exit(0)
    elif(d>29):
        print("-1")
        sys.exit(0)
    else:
        print_season(m)
        sys.exit(0)
else:
    print_season(m)