n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
direction = -1  # 처음에는 아래에서 위로 채움
j = n - 1

while j >= 0:
    if direction == -1:
        for i in range(n - 1, -1, -1):  # 아래에서 위로
            arr[i][j] = cnt
            cnt += 1
    else:
        for i in range(n):  # 위에서 아래로
            arr[i][j] = cnt
            cnt += 1

    direction *= -1  # 방향 전환
    j -= 1  # 열을 왼쪽으로 이동

# 배열 출력
for row in arr:
    print(" ".join(map(str, row)))