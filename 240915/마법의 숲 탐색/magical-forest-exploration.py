from sys import stdin
from collections import deque

R, C, K = map(int, stdin.readline().split())
board = [[0] * C for _ in range(R)]
res = 0  # 정령들이 최종적으로 위치한 행의 총합

def move(center_i, center_j, exit_dir):
    # 먼저 최종 행을 본인의 골렘의 남쪽으로 계산
    max_i = center_i + 1

    # 본인 골렘 출구 위치
    if exit_dir == 0:
        exit_i, exit_j = center_i - 1, center_j
    elif exit_dir == 1:
        exit_i, exit_j = center_i, center_j + 1
    elif exit_dir == 2:
        exit_i, exit_j = center_i + 1, center_j
    elif exit_dir == 3:
        exit_i, exit_j = center_i, center_j - 1
    # bfs로 최종 위치 계산 위한 방문 보드 배열
    visited = [[0] * C for _ in range(R)]
    visited[center_i][center_j], visited[center_i - 1][center_j], visited[center_i][center_j + 1], visited[center_i + 1][center_j], visited[center_i][center_j - 1] = 1, 1, 1, 1, 1
    queue = deque()
    queue.append((exit_i, exit_j))
    while queue:
        i, j = queue.popleft()
        max_i = max(max_i, i)
        for di, dj in ((1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni <R and 0 <= nj <C and board[ni][nj] != 0 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = 1
    return max_i + 1


def marking(center_i, center_j, exit_dir):
    board[center_i][center_j] = 1
    if exit_dir == 0:
        board[center_i -1][center_j] = 2
        board[center_i][center_j + 1] = 1
        board[center_i + 1][center_j] = 1
        board[center_i][center_j - 1] = 1
    elif exit_dir == 1:
        board[center_i -1][center_j] = 1
        board[center_i][center_j + 1] = 2
        board[center_i + 1][center_j] = 1
        board[center_i][center_j - 1] = 1
    elif exit_dir == 2:
        board[center_i -1][center_j] = 1
        board[center_i][center_j + 1] = 1
        board[center_i + 1][center_j] = 2
        board[center_i][center_j - 1] = 1
    elif exit_dir == 3:
        board[center_i -1][center_j] = 1
        board[center_i][center_j + 1] = 1
        board[center_i + 1][center_j] = 1
        board[center_i][center_j - 1] = 2


for _ in range(K):
    golem_start_c, golem_exit_d = map(int, stdin.readline().split())
    golem_center_c = golem_start_c - 1
    golem_center_r = -2
    while 1:
        # 끝에 도달
        if golem_center_r == R - 2:
            marking(golem_center_r, golem_center_c, golem_exit_d)
            res += R
            break
        # 처음 시작 할 때부터 막히는 경우
        if golem_center_r == -2 and board[golem_center_r + 2][golem_center_c] != 0:
            board = [[0] * C for _ in range(R)]
            break

        # 남쪽으로 내려갈 때 막히면, 서쪽이나 동쪽 회전 알아봐야됨
        if golem_center_r != -2 and (board[golem_center_r + 2][golem_center_c] != 0 or board[golem_center_r + 1][golem_center_c - 1] != 0 or board[golem_center_r + 1][golem_center_c + 1] != 0):
            # 서쪽 회전 되는지 확인
            if 0 <= (golem_center_c - 2) and board[golem_center_r - 1][golem_center_c -1] == 0 and board[golem_center_r][golem_center_c - 2] == 0 and board[golem_center_r + 1][golem_center_c - 1] == 0 and board[golem_center_r + 1][golem_center_c - 2] == 0 and board[golem_center_r + 2][golem_center_c - 1] == 0:
                # 서쪽 회전 가능
                golem_center_r, golem_center_c = golem_center_r + 1, golem_center_c - 1
                # 출구 방향 바꾸기
                if golem_exit_d == 0:
                    golem_exit_d = 3
                else:
                    golem_exit_d -= 1

            # 안 되면 동쪽 회전 되는지 확인
            elif (golem_center_c + 2) < C and board[golem_center_r - 1][golem_center_c + 1] == 0 and board[golem_center_r][golem_center_c + 2] == 0 and board[golem_center_r + 1][golem_center_c + 1] == 0 and board[golem_center_r + 1][golem_center_c + 2] == 0 and board[golem_center_r + 2][golem_center_c + 1] == 0:
                # 동쪽 회전 가능
                golem_center_r, golem_center_c = golem_center_r + 1, golem_center_c + 1
                # 출구 방향 바꾸기
                if golem_exit_d == 3:
                    golem_exit_d = 0
                else:
                    golem_exit_d += 1

            # 골렘의 몸 일부가 여전히 숲을 벗어난 상태
            elif golem_center_r - 1 < 0:
                board = [[0] * C for _ in range(R)]
                break

            # 막혔는데, 보드 안에 안착하고, 회전 안 되면 보드에 마킹 후 종료
            else:
                marking(golem_center_r, golem_center_c, golem_exit_d)
                max_row = move(golem_center_r, golem_center_c, golem_exit_d)
                res += max_row
                break

        # 막히지 않으면 계속해서 내려가기
        else:
            golem_center_r += 1

        # print("center_r, center_c", golem_center_r, golem_center_c)

    # for b in board:
    #     print(*b)
    # print("res", res)

print(res)