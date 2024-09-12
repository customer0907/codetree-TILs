import sys

a,b = sys.stdin.readline().split()

def calTwoNum(_a, _b):
    if(_a < _b):
        _a += 10
        _b *= 2
    else:
        _a *=2
        _b += 10
    return _a,_b
    
a = int(a)
b = int(b)

a,b = calTwoNum(a,b)

print(a,b)