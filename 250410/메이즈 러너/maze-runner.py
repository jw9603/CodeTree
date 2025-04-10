################################### 문제 이해 ###################################
# M명의 참가자가 미로 탈출하기 게임에 참가하였습니다.
# 미로의 구성은 다음과 같다.
# 1. 미로는 N x N 크기의 격자입니다. 좌상단은 (1, 1)입니다.
# 2. 미로의 각 칸은 다음 3가지 중 하나의 상태를 갖습니다.
    # 1. 빈 칸: 참가자가 이동 가능한 칸입니다.
    # 2. 벽: 
        # 참가자가 이동할 수 없는 칸입니다.
        # 1이상 9이하의 내구도를 갖고 있습니다.
        # 회전할 때, 내구도가 1씩 깎입니다. -> 회전을 어떻게 한다는 거지?
        # 내구도가 0이 되면, 빈 칸으로 변경된다.
    # 3. 출구: 참가자가 해당 칸에 도달하면, 즉시 탈출한다.

# 1초마다 모든 참가자는 한 칸씩 움직인다. 움직이는 조건은 다음과 같습니다.

# 두 위치 (x1, y1), (x2, y2)의 최단 거리는 맨해튼 거리
# 모든 참가자는 동시에 움직인다. 동시에!!!@@@@@@@@@
# 상하좌우로 움직일 수 있으며, 벽이 없는 곳으로 이동 가능
# 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단거리가 가까워야 한다.
# 움직일 수 있는 칸이 2개 이상이라면, 상하로 움직이는 것을 우선시
# 참가자가 움직일 수 없는 상황이라면 움직이지 않는다.
# 한 칸에 2명 이상의 참가자가 있을 수 있다. -> 일반적인 해당 (x, y)좌표에 한 칸만 들어가는 형태의 자료형은 X

# 모든 참가자가 이동을 끝냈으면, 다음 조건에 의해 미로가 회전한다.
# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다.
# 가장 작은 크기를 갖는 정사각형이 2개 이상이라면, 좌상단 r좌표가 작은 것이 우선되고, 그래도 같으면 c좌표가 작은 것이 우선
# 선택된 정사각형은 시계 방향으로 90도 회전하며, 회전된 벽은 내구도가 1씩 깍입니다.

# K초 동안 위의 과정을 계속 반복된다.
# 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝남
# 게임이 끝났을 때, 모든 참가자들의 이동 거리 합과 출구 좌표를 출력하는 프로그램을 작성

################################### 문제 이해 ###################################
################################### 알고리즘 ###################################
# 입력
# N, M, K가 주어진다.
# 다음 N개의 줄에 걸쳐서 N x N 크기의 미로에 대한 정보가 주어진다.
# 0이라면, 빈 칸, 1이상 9이하의 값을 갖는다면, 벽이며 내구도
# 다음 M개의 줄에 걸쳐서 참가자의 좌표가 주어진다. 
# 다음 줄에 출구의 좌표가 주어진다.

# 출력
# 게임 시작 후 K초가 지났거나, 모든 참가자가 미로를 탈출했을 때, 모든 참가자들의 이동 거리 합과 출고 좌표를 출력

# 1. 매 초마다.
# 2. 모든 참가자가 동시에 1칸 움직인다.

# 3. 그 다음 미로가 회전한다.
################################### 알고리즘 ###################################
# def move_players(N, board, ei, ej):
#     total_moves = 0
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     new_board = [row[:] for row in board]
#     escaped = 0

#     for i in range(N):
#         for j in range(N):
#             if -11 < board[i][j] < 0:
#                 dist = abs(ei - i) + abs(ej - j)
#                 for di, dj in directions:  # 상하좌우로 움직일 수 있으며
#                     ni, nj = i + di, j + dj
                    
#                     # 벽이 없는 곳이여야 하며 움직인 칸은 현재 머물러 있던 칸보다 출구까지의 최단 거리가 가까워야 한다.
#                     if 0 <= ni < N and 0 <= nj < N and board[ni][nj] <= 0 and dist > abs(ei - ni) + abs(ej - nj):
#                         total_moves += board[i][j]
#                         new_board[i][j] -= board[i][j]
                        
#                         # 도착한 곳이 출구가 아니라면, 참가자 수 만큼 해당 칸에 더함
#                         if board[ni][nj] != -11:
#                             new_board[ni][nj] += board[i][j]
#                         else:
#                             escaped += -board[i][j]
#                         break

#     return new_board, total_moves, escaped

# def rotate(board, N, ei, ej):
#     '''
#     한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡는다.
#     '''
#     si, sj, l = find_square(board, N, ei, ej)
#     tmp = [row[:] for row in board]
#     for i in range(l):
#         for j in range(l):
#             tmp[si + i][sj + j] = board[si + l - 1 - j][sj + i]
#             if tmp[si + i][sj + j] > 0:
#                 tmp[si + i][sj + j] -= 1

#     return tmp


# def find_square(board, N, ei, ej):
#     '''
#     한 명 이상의 참가자와 출구를 무조건 포함하는 가장 작은 정사각형
#     '''
#     row_len = N
#     for i in range(N):
#         for j in range(N):
#             if -11 < board[i][j] < 0:
#                 row_len = min(row_len, max(abs(ei - i), abs(ej - j)))

#     for si in range(N - row_len):
#         for sj in range(N - row_len):
#             if si <= ei <= si + row_len and sj <= ej <= sj + row_len:
#                 for i in range(si, si + row_len + 1):
#                     for j in range(sj, sj + row_len + 1):
#                         if -11 < board[i][j] < 0:
#                             return si, sj, row_len + 1



# def simulate(N, M, K, board, ei, ej):
#     total_distance = 0
#     cnt = M

#     for _ in range(K): #  매 초마다
#         # 1. 모든 참가자가 동시에 1칸 움직인다.
#         board, moved, escaped = move_players(N, board, ei, ej)
#         total_distance -= moved

#         cnt -= escaped

#         # 만약 K초 전에 모든 참가자가 탈출에 성공한다면 게임이 끝난다.
#         if cnt == 0:
#             break
        
#         # 미로가 회전
#         board = rotate(board, N, ei, ej)
    
#         for i in range(N):
#             for j in range(N):
#                 if board[i][j] == -11:
#                     ei, ej = i, j # 출구의 위치를 업데이트

#     return total_distance, ei + 1, ej + 1

# def main():
#     N, M, K = map(int, input().split())

#     # board에 0은 빈 칸, 1~9는 벽, -1은 사람
#     board = [list(map(int, input().split())) for _ in range(N)]

#     for _ in range(M):
#         i, j = map(lambda x: int(x) - 1, input().split())
#         board[i][j] -= 1 # 한 칸에 2명 이상의 참가자가 있을 수 있다.
    
#     ei, ej = map(lambda x: int(x) - 1, input().split())
#     board[ei][ej] = -11 # 출구

#     total_move, exit_i, exit_j = simulate(N, M, K, board, ei, ej)

#     print(total_move)
#     print(exit_i, exit_j)

# if __name__ == '__main__':
#     main()

def move_players(N, board, ei, ej):
    '''
    모든 참가자들은 동시에 1칸씩 움직인다.
    (ei, ej) : 출구
    
    '''
    total_move = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new_board = [row[:] for row in board]
    escaped = 0

    for i in range(N):
        for j in range(N):
            if -11 < board[i][j] < 0:
                # 이 조건문에 들어왔다는 것은 (i, j)에 참가자가 있다는 것
                dist = abs(ei - i) + abs(ej - j)
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    # (ni, nj)에 벽이 없어야 한다.
                    # (ni, nj)와 (ei, ej)의 거리가 dist보다 작아야 한다.
                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] <= 0 and dist > abs(ni - ei) + abs(nj - ej):
                        total_move += board[i][j]
                        new_board[i][j] -= board[i][j]

                        if board[ni][nj] != -11:
                            new_board[ni][nj] += board[i][j]
                        else:
                            escaped += -board[i][j]
                        
                        break
    return new_board, total_move, escaped

def find_square(board, N, ei, ej):
    row_len = N

    for i in range(N):
        for j in range(N):
            if -11 < board[i][j] < 0:
                row_len = min(row_len, max(abs(ei - i), abs(ej - j)))
    
    for si in range(N - row_len):
        for sj in range(N - row_len):
            if si <= ei <= si + row_len and sj <= ej <= sj + row_len:
                for i in range(si, si + row_len + 1):
                    for j in range(sj , sj + row_len + 1):
                        if -11 < board[i][j] < 0:
                            return si, sj, row_len + 1
                        
def rotate(board, N, ei, ej):
    si, sj, L = find_square(board, N, ei, ej) 
    tmp = [row[:] for row in board]

    for i in range(L):
        for j in range(L):
            tmp[si + i][sj + j] = board[si + L - 1 - j][sj + i]
            if tmp[si + i][sj + j] > 0:
                tmp[si + i][sj + j] -= 1
    
    return tmp

def simulate(N, M, K, board, ei, ej):
    total_distance = 0
    cnt = M # 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝난다.
    for _ in range(K):
        # 1. 모든 참가자들이 움직인다.
        board, moved, escaped = move_players(N, board, ei, ej)
        total_distance -= moved
        cnt -= escaped

        # 2. 만약 K초 전에 모든 참가자가 탈출에 성공한다면, 게임이 끝난다.
        if cnt == 0:
            break
        
        # 3. 미로가 회전한다.
        board = rotate(board, N, ei, ej)

        # 4. 회전 후 출구 업데이트
        for i in range(N):
            for j in range(N):
                if board[i][j] == -11:
                    ei, ej = i, j
    
    return total_distance, ei + 1, ej + 1
        
def main():
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    for _ in range(M):
        i, j = map(lambda x: int(x) - 1, input().split())
        board[i][j] -= 1
    
    # 출구
    ei, ej = map(lambda x: int(x) - 1, input().split())
    board[ei][ej] = -11

    total_move, exit_i, exit_j = simulate(N, M, K, board, ei, ej)
    print(total_move)
    print(exit_i, exit_j)

if __name__ == '__main__':
    main()