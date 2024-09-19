import sys

n = input()

num_arr = list(map(int,sys.stdin.readline().split()))
arr_bag = []

def median_num(arr):
    for i in range(len(arr)):
        arr_bag.append(arr[i])
        arr_bag.sort()
        if i == 0 or i % 2 == 0:
            print(arr_bag[(len(arr_bag)//2)],end=' ')
        else:
            continue

median_num(num_arr)