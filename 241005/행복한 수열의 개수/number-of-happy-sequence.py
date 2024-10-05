from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
result = 0


for i in range(n):
    sequence = 0
    for j in range(1, n):
        if board[i][j] == board[i][j-1]:
            sequence += 1
        else:
            sequence = 0
        
        if sequence == m - 1:
            result += 1
            break



for j in range(n):
    sequence = 0
    for i in range(1, n):
        if board[i][j] == board[i-1][j]:
            sequence += 1
        else:
            sequence = 0
        
        if sequence == m - 1:
            result += 1
            break

if n == 1:
    result = 2
print(result)