############################################## 문제 이해 ##############################################

# N x N의 미지의 공간에 갇힘
# 타임머신을 타고 이 공간에서 탈출해야 한다.

# 이 공간은 한 변의 길이가 N인 2차원 평면이며, 그 사이 어딘가에는 한변의 길이가 M인 정육면체 형태의 시간의 벽이 세워져있다.

# 이 평면도와 단면도는 빈 공간(0)과 장애물(1)로 구성되어 있다.
# 타임머신은 빈 공간만 이동할 수 있다. -> BFS에 쓰일것 같다.

# 타임머신은 시간의 벽의 윗면 어딘가에 위치,
# 시간의 벽의 윗면 단면도에서는 타임머신의 위치 2가 추가로 표시된다.

# 마찬가지로 미지의 공간 평면도에서는 시간의 벽의 위치 3과 탈출구 4
# 탈출구는 시간의 벽 외부에 있는 미지의 공간의 바닥에 위치

# 시간의 벽과 맛닿은 미지의 공간의 바닥은 기본적으로 장애물들로 둘러 쌓여있다.
# 그러나 단 한 칸만 빈 공간으로 뚫려 있기 때문에 시간의 벽에서 미지의 공간 바닥으로 이어질 수 있는 출구는 하나다.

# 미지의 공간의 바닥에는 총 F개의 시간 이상 현상이 존재
# 각 시간 이상 현상은 바닥의 빈 공간 (ri, ci)에서 시작하여 매 vi의 배수턴마다 방향 di로 한 칸씩 확산되며
# 확산된 이후에도 기존 위치의 시간 이상 현상은 사라지지 않고 남아 있다.

# 시간 이상 현상은 장애물(1)과 탈출구가 없는 빈 공간으로만 확산되며, 확산된 이후에도 기존 위치의 시간 이상 현상은 
# 사라지지 않고 남아 있다.
# 모든 시간 이상 현상(F개)은 서로 독립적이며 동시에 확산된다. 방향d는 동(0), 서(1), 남(2), 북(3)

# 또 턴이 나온다..

# 타임머신은 매 턴마다 상하좌우로 한 칸씩 이동, 장애물(1)과 시간 이상 현상을 피해 탈출구까지 도달해야 한다.
# 타임머신이 시작점에서 탈출구까지 이동하는 데 필요한 최소 시간(턴 수)을 출력하라!!

# 만약 탈출할 수 없다면 -1을 출력

# 시간 이상 현상이 확산되고 나서 타임머신 이동!
############################################## 문제 이해 ##############################################

############################################## 알고리즘 빌드업 ##############################################
# 입력
# N(한변의 길이), M(시간의 벽 한 변의 길이) -> 정육면체, F(시간 이상 현상의 개수)가 한 줄에 공백을 두고 주어짐
# 미지의 공간의 평면도가 주어짐 -> N * N의 평면도
# 시간의 벽의 동, 서, 남, 북, 윗면의 단면도가 각각 M 줄에 걸쳐 차례로 주어짐.
# F 줄에 걸쳐 각 시간 이상 현상의 초기 위치 ri, ci와 확산 방향 di, 확산상수 vi가 주어짐

# 출력
# 타임머신이 시작점에서 탈출구까지 이동하는 데 필요한 최소 시간 (턴 수)을 출력
# 탈출할 수 없다면 -1 출력

# 알고리즘
# 일단 매 턴이 있음
# 한 턴동안 각 행동들의 순서 정리가 필요: 1. 시간 이상 현상의 확산, 2. 확산된 맵을 반환받고 이 맵에서 타임머신의 이동
# 물론 시간 이상 현상은 매 턴마다 진행은 X -> 매 vi의 배수 턴마다 확산

# 1. 시간 이상 현상의 확산 -> 일단 이건 일반적인 2차원이기 때문에 기본적인 BFS를 적용 가능
# 시간 이상 현상도 동(0), 서(1), 남(2), 북(3)으로 확산 
# 

# 2. 확산된 맵을 반환받고 이 맵에서 타임머신의 이동 ->이게 문제,,, 3차원이고, 3차원 정육면체의 남(밑면)이 평면도와 닿는 구간을 3으로 표시됨
# 출발지는 시간의 벽의 윗면임(타임머신의 위치 2)
# Goal: 탈출구(4)로 최소 시간(턴 수) 도착
# 타임머신은 상, 하, 좌, 우로 이동 가능


############################################## 알고리즘 빌드업 ##############################################

from collections import deque
def find_3d_start(M, board3):
    '''
    타임머신의 출발 지점 좌표 파악
    '''
    for i in range(M):
        for j in range(M):
            if board3[i][j] == 2:
                return 4, i, j

def find_2d_end(N, board):
    '''
    탈출구 
    '''
    for i in range(N):
        for j in range(N):
            if board[i][j] == 4:
                board[i][j] = 0
                return i, j

def find_wall_base(N, board):
    '''
    시간의 벽 시작 지점 (3으로 표시된 위치 중 첫 번째 지점)
    '''
    for i in range(N):
        for j in range(N):
            if board[i][j] == 3:
                return i, j

def find_wall_exit(N, M, board):
    '''
    시간의 벽 내부에서 외부 바닥으로 연결되는 유일한 출구 찾기
    return: (벽 위치, 정육면체에서 한 평면에서의 i, 정육면체에서 한 평면에서의 j, 실제 평면도 좌표에서의 i, j)
    '''
    base_i, base_j = find_wall_base(N, board)
    for i in range(base_i, base_i + M):
        for j in range(base_j, base_j + M):
            if board[i][j] != 3:
                continue
            
            if board[i][j + 1] == 0:    # 3 시작 지점 기준으로 우측 한 칸
                return 0, M - 1, M - 1 - (i- base_i), i, j + 1
            elif board[i][j - 1] == 0:  # 3 시작 지점 기준으로 좌측 한 칸
                return 1, M - 1, M - 1, i - base_i, i, j - 1
            elif board[i + 1][j] == 0:  # 3 시작 지점기준으로 아래 한 칸
                return 2, M - 1, j - base_j, i + 1, j
            elif board[i - 1][j] == 0:  # 3 시작 지점 기준으로 위 한 칸
                return 3, M - 1, M - 1 - (j - base_j),i - 1, j
    
# 포기,,,! -> 좌표 변환 실패
def bfs_3d(board3, M, st, si, sj, et, ei, ej):
    global left_nxt, right_nxt

    queue = deque([(st, si, sj)])
    visited = [[[0] * M for _ in range(M)] for _ in range(5)]  # 동, 서, 남, 북, 윗면
    visited[st][si][sj] = 1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        ct, ci, cj = queue.popleft()

        if (ct, ci, cj) == (et, ei, ej):
            return visited[ct][ci][cj]
        
        for di, dj in directions:
            ni, nj = ci + di, cj + dj

            if ni < 0: # 위쪽 범위 
                if ct == 0:
                    nt, ni, nj = 4, (M - 1) - cj,M - 1
                elif ct == 1:
                    nt, ni, nj = 4, cj, 0
                elif ct == 2:
                    nt, ni, nj = 4, M - 1, cj
                elif ct == 3:
                    nt, ni, nj = 4, 0, (M - 1) - cj
                elif ct == 4:
                    nt, ni, nj = 3, 0, (M - 1) - cj
            
            elif ni >= M: # 아래쪽
                if ct == 4:
                    nt, ni, nj = 2, 0, cj
                else:
                    continue
            
            elif nj < 0: # 왼쪽
                if ct == 4:
                    nt, ni, nj = 1, 0, ci
                else:
                    nt, ni, nj = left_nxt[ct], ci, M - 1 - ci

            elif nj >= M: # 오른쪽
                if ct == 4:
                    nt, ni, nj = 0, 0, (M - 1) - ci
                else:
                    nt, ni, nj = right_nxt[ct], ci, 0

            else:
                nt = ct
            
            if visited[nt][ni][nj] == 0 and board3[nt][ni][nj] == 0:
                visited[nt][ni][nj] = visited[ct][ci][cj] + 1
                queue.append((nt, ni, nj))

    return -1


def simulate_anomalies_and_generate_time_map(N, board, diffusion, exit_i, exit_j):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    time = [[1000] * N for _ in range(N)] # 시간 이산 현상이 해당 칸에 언제 도달하는 지를 저장한 시간 지도

    for di, dj, dd, dv in diffusion:
        time[di][dj] = 1

        for mul in range(1, N + 1):
            di += directions[dd][0]
            dj += directions[dd][1]

            if 0 <= di < N and 0 <= dj < N and board[di][dj] == 0 and (di, dj) != (exit_i, exit_j):
                if time[di][dj] > dv * mul:
                    time[di][dj] = dv * mul
            else:
                break
    return time

def bfs_2d(N, board, time, start_i, start_j, end_i, end_j, start_time):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(start_i, start_j)])
    time[start_i][start_j] = start_time

    while queue:
        cur_i, cur_j = queue.popleft()
        if (cur_i, cur_j) == (end_i, end_j):
            return time[cur_i][cur_j]
        
        for di, dj in directions:
            next_i, next_j = cur_i + di, cur_j + dj

            if 0 <= next_i < N and 0 <= next_j < N:
                if board[next_i][next_j] == 0 and time[cur_i][cur_j] + 1 < time[next_i][next_j]:
                    time[next_i][next_j] = time[cur_i][cur_j] + 1
                    queue.append((next_i, next_j))
    
    return -1

def main():
    global left_nxt, right_nxt
    N, M, F = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    board3 = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)] # 동, 서, 남, 북, 윗면
    diffusion = [list(map(int, input().split())) for _ in range(F)]

    # 1. 각 위치들의 좌표를 찾는다.
    # 시간의 벽에서 타임머신의 위치
    st, si, sj = find_3d_start(M, board3[4])

    # 타임머신의 목표 지점
    exit_i, exit_j = find_2d_end(N, board)

    # 시간의 벽에서 미지의 공간의 바닥으로 이어질 수 있는 출구
    et, ei, ej, si2, sj2  = find_wall_exit(N, M, board)


    # 평면 이동 정보 (전개도 규칙)
    left_nxt = {0: 2, 2: 1, 1: 3, 3: 0}
    right_nxt = {0: 3, 2: 0, 1: 2, 3: 1}

    # 2. 타임머신 출발점에서 바닥 출구까지의 거리
    dist = bfs_3d(board3, M, st, si, sj, et, ei, ej) # 실패

    if dist != -1:
        # 이상 현상 처리 후 2D 탈출
        time = simulate_anomalies_and_generate_time_map(N, board, diffusion, exit_i, exit_j)
        dist = bfs_2d(N, board, time, si2, sj2, exit_i, exit_j, dist)
    print(dist)

if __name__ == '__main__':
    main()