n, r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

si, sj = r - 1, c - 1
while 1:
    print(board[si][sj], end=' ')
    move_flag = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni = si + di
        nj = sj + dj
        if not (0<= ni < n and 0<= nj < n):
            continue
        if board[ni][nj] > board[si][sj]:
            si, sj = ni, nj
            move_flag = 1
            break
    
    if move_flag == 0:
        break