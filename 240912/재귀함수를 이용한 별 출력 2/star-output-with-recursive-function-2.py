num = int(input())

def recursion_star(n):
    if(n>0):
        print("* "*n)
        recursion_star(n-1)
    elif(n==0):
        recursion_star(n-1)
    else:
        print("* "*(-n))
        if(-n == num):
            return
        recursion_star(n-1)

recursion_star(num)