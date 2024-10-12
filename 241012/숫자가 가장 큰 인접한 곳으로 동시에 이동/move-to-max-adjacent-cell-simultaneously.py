n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

count = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    count[x-1][y-1] = 1

for _ in range(t):
    next_count = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                max_value = 0 
                mi, mj = -1, -1
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if not (0<= ni < n and 0 <= nj < n):
                        continue
                    if board[ni][nj] > max_value:
                        max_value = board[ni][nj]
                        mi, mj = ni, nj
                next_count[mi][mj] += 1

    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                count[i][j] = 0
            else:
                count[i][j] = next_count[i][j]
    
res = 0
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            res += 1

print(res)