n = int(input())

def print_rec(n):
    cnt = 1
    for i in range(n):
        for j in range(n):
            if(cnt==10):
                cnt=1
            print(cnt,end=' ')
            cnt+=1
        print()

print_rec(n)