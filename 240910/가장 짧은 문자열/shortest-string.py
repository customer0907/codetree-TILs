import sys

arr = []
for i in range(3):
    arr.append(sys.stdin.readline().strip())

int_arr = [len(s) for s in arr]
int_arr.sort()

print(int_arr[-1]-int_arr[0])