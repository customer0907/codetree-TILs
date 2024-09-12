import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

max_val = 0

def max_recursion(idx,_arr):
    global max_val
    if(len(_arr)==idx):
        return
    if(max_val < _arr[idx]):
        max_val = _arr[idx]
    max_recursion(idx+1,_arr)
    return max_val

max_val = max_recursion(0,arr)
print(max_val)