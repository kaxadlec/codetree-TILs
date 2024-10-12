n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

falling_block = [0]*n
for j in range(k-1, k-1+m):
    falling_block[j] = 1

stop_i = n-1
for i in range(1, n):
    stop_flag = 0
    for j in range(n):
        if falling_block[j] == 1 and board[i][j] == 1:
            stop_flag = 1
            break
    if stop_flag == 1:
        stop_i = i - 1
        break

for j in range(k-1, k-1+m):
    board[stop_i][j] = 1

for row in board:
    print(*row)