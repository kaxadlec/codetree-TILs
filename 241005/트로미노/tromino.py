from sys import stdin

n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

shapes = [[(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (0, 1)], [(0, 0), (0, 1), (1, 1)], [(1, 0), (0, 1), (1, 1)], [(0, 0), (0, 1), (0, 2)], [(0, 0), (1, 0), (2, 0)]]

max_sum = 0
for i in range(n):
    for j in range(m):
        shapes_sum = 0
        for shape in shapes:
            shape_sum = 0
            for cd in shape:
                ni = i + cd[0]
                nj = j + cd[1]
                if not (0<=ni<n and 0<=nj<m):
                    continue
                shape_sum += board[ni][nj]

            shapes_sum = max(shapes_sum, shape_sum)


        max_sum = max(max_sum, shapes_sum)


print(max_sum)