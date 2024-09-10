time = input()

h,m = map(int,time.split(":"))

h = (h+1)%24

print(f"{h}:{m}")