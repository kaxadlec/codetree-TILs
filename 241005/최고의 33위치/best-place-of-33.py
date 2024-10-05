from sys import stdin

n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

max_cnt = 0
for i in range(n-2):
    for j in range(n-2):
        sum = 0
        for r in range(i, i+3):
            for c in range(j, j+3):
                sum += board[r][c]
        max_cnt = max(max_cnt, sum)

print(max_cnt)