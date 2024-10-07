import sys

N = int(sys.stdin.readline())

arr = []
is_overlap = [0] * 101  # 최대 범위를 고려하여 크기 조정

for _ in range(N):
    x1, x2 = map(int, sys.stdin.readline().split())
    arr.append((x1, x2))

for x1, x2 in arr:
    for j in range(x1, x2 + 1):
        is_overlap[j] += 1

print(max(is_overlap))