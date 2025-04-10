########################################### 문제 이해 ###########################################
#  N x M 격자가 있고, 모든 위치에는 포탑이 존재한다. (즉, 포탑의 개수는 NM개)
# 각 포탑에는 공격력이 존재, 상황에 따라 공격력이 줄어들거나 늘어날 수 있다.
# 또한, 공격력이 0이하가 된다면, 해당 포탑은 부서지며 더 이상의 공격을 할 수 없다.

# 최초에 공격력이 0인 포탑 즉, 부서진 포탑이 존재할 수 있다.

# 하나의 턴은 다음의 4가지 액션을 순서대로 수행하며, 총 K번 반복된다.
# 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지

# 1. 공격자 선정
# 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정
# 공격자로 선정되면 가장 약한 포탑이므로, N + M만큼의 공격력이 증가된다.

# 가장 약한 포탑은 다음의 기준으로 선정
# 1.1 공격력이 가장 낮은 포탑이 가장 약한 포탑
# 1.2 만약 공격력이 가장 낮은 포탑이 2개 이상이라면, 가장 최근에 공격한 포탑이 가장 약한 포탑
# 1.3 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑이 가장 약한 포탑
# 1.4 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑이 가장 약한 포탑
# 우선순위: 공격력이 가장 낮은 -> 가장 최근에 공격 -> 행과 열의 합이 가장 큰 포탑 -> 열 값이 가장 큰 포탑

# 2. 공격자의 공격
# 선정된 공격자는 자신을 제외한 가장 강한 포탑을 공격한다.

# 가장 강한 포탑은 위에서 정한 가장 약한 포탑의 반대 기준
# 2.1 공격력이 가장 높은 포탑
# 2.2 공격력이 가장 높은 포탑이 2개 이상이라면, 공격한 지 가장 오래된 포탑이 가장 강한 포탑 
# 2.3 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑이 가장 강한 포탑
# 2.4 만약 그러한 포탑이 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑
# 우선순위: 공격력이 가장 높은 -> 가장 최근에 공격 -> 행과 열의 합이 가장 작은 -> 열 값이 가장 작은 포탑

# 공격을 할 때에는 레이저 공격을 먼저 시도하고, 만약 그게 안 된다면 포탄 공격

# 1. 레이저 공격
# 1.1 상하좌우의 4개 방향
# 1.2 부서진 포탑이 있는 위치는 지날 수 없다. 부서졌다? 공격력 0
# 1.3 가장자리에서 막힌 방향으로 진행하고자 한다면, 반대편으로 나온다.

# 레이저 공격은 공격자의 위치에서 공격 대상 포탑까지의 최단경로로 공격합니다.
# 만약 그러한 경로가 존재하지 않는다면 포탄 공격을 진행합니다.
# 만약 경로의 길이가 똑같은 최단 경로가 2개 이상이라면, 우 -> 하 -> 좌 -> 상의 우선순위대로 먼저 움직인 경로가 선택

# 최단 경로가 정해졌으면, 공격 대상에는 공격자의 공격력만큼 피해를 입으며, 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어듭니다.

# 2. 포탄 공격
# 공격 대상(공격 당하는 포탑)은 공격자 공격력 만큼의 피해를 받는다. 추가적으로 주위 8개의 방향에 있는 포탑도 피해를 입는다.
# 공격자 공격력의 절반 만큼 피해를 받는다.
# 만약 가장 자리에 포탄이 떨어졌다면, 위에서의 레이저 이동처럼 포탄의 추가 피해가 반대편 격자에 미치게 된다.

# 3. 포탑 부서짐
# 공격력이 0이 되면 부서짐

# 4. 포탑 정비
# 공격이 끝났으면, 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력이 1씩 올라간다.
# 공격과 무관하다는 뜻은 공격자도 아니고, 공겨의 피해를 입은 포탑도 아니라는 뜻
########################################### 문제 이해 ###########################################
########################################### 알고리즘 ###########################################
# 입력
# N, M, K가 주어짐
# 두번째 줄부터 N개의 줄에 걸쳐서 N * M 격자에 대한 정보가 주어짐.
# 출력
# 첫 번째 줄에 K번의 턴이 종료된 후 남아있는 포탑 중 가장 강한 포탑의 공격력을 출력

# 필요한 변수?
# 1. 입력값들
# 2. 각 포탑들이 언제 최근에 공격했는지를 담는 리스트

# 쓰이는 알고리즘
# 1. BFS(레이저 공격, )
    # 레이저 공격이 가능하다면,,!
    # 레이저 공격이 불가능하면 -> 포탄 공격을 수행 -> BFS가 아닌 공격 대상에게 수행
# 2. 각 포탑들이 언제 최근에 공격햇는지를 계속 업데이트 필요

########################################### 알고리즘 ###########################################
from collections import deque
def bfs(N, M, board, si, sj, ei, ej):
    global fight_set
    '''
    레이저 공격
    부서진 포탑(0)이 있는 위치는 지날 수 없다.
    가장자리에서 막힌 방향이면 반대편으로 나온다. -> %계산
    레이저 공격은 공격자의 위치에서 공격 대상 포탑까지의 최단 경로로 공격
    만약 그러한 경로가 존재하지 않는다면 포탄 공격
    우 하 좌 상의 우선순위
    '''
    queue = deque([(si, sj)])
    directions1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[] for _ in range(M)] for _ in range(N)]
    visited[si][sj] = (si, sj)
    attack_power = board[si][sj]

    while queue:
        ci, cj = queue.popleft()
        
        # 레이저가 도착햇으면 경로를 역추적하면서 피해 계산
        if (ci, cj) == (ei, ej):
            board[ei][ej] = max(0, board[ei][ej] - attack_power)
            while True:
                ci, cj = visited[ci][cj]
                if (ci, cj) == (si, sj):
                    return True
                board[ci][cj] = max(0, board[ci][cj] - attack_power // 2)
                fight_set.add((ci, cj))
        
        for di, dj in directions1:
            ni, nj = (ci + di) % N, (cj + dj) % M
            if not visited[ni][nj] and board[ni][nj] > 0:
                queue.append((ni, nj))
                visited[ni][nj] = (ci, cj)
    
    return False

def bomb(N, M, board, si, sj, ei, ej):
    global fight_set
    '''
    공격 대상은 공격자의 공격력만큼 피해를 받는다.
    추가적으로 주위 8개의 방향에 있는 포탑도 피해를 입는다. -> 공격력의 절반 만큼의 피해를 받는다.
    공격자는 영향을 받지 않는다.
    만약 가장자리에 포탄이 떨어졌다면, 포탄의 추가 피해가 반대편 격자에 미치게 된다.
    '''
    attack_power = board[si][sj]
    directions2 = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]

    for di, dj in directions2:
        ni, nj = (ei + di) % N, (ej + dj) % M
        if (ni, nj) != (si, sj):
            board[ni][nj] = max(0, board[ni][nj] - attack_power // 2)
            fight_set.add((ni, nj))

def simulate(N, M, K, board, attack_turn):
    global fight_set

    for t in range(1, K + 1):
        min_power, max_turn, si, sj = 5001, 0, -1, -1
        # 1. 공격자 선정: 공격력이 가장 낮은 포탑부터 탐색
        for i in range(N):
            for j in range(M):
                if board[i][j] <= 0:
                    continue
                
                if min_power > board[i][j] or (min_power == board[i][j] and max_turn > attack_turn[i][j]) or (min_power == board[i][j] and max_turn == attack_turn[i][j] and si +sj < i + j) or (min_power == board[i][j] and max_turn == attack_turn[i][j] and si + sj == i + j and sj < j):
                    min_power, max_turn, si, sj = board[i][j], attack_turn[i][j], i, j
        
        # 2. 공격을 받는 대상자 선정: 공격력이 가장 강한 포탑을 공격
        max_power, min_turn, ei, ej = 0, t, N, M
        for i in range(N):
            for j in range(M):
                if board[i][j] <= 0:
                    continue
                
                if max_power < board[i][j] or (max_power == board[i][j] and min_turn < attack_turn[i][j]) or (max_power == board[i][j] and min_turn == attack_turn[i][j] and ei + ej > i + j) or (max_power == board[i][j] and min_turn == attack_turn[i][j] and ei + ej== i + j and ej > j): 
                    max_power, min_turn, ei, ej = board[i][j], attack_turn[i][j], i, j

        # 3. 공격자의 공격력 증가
        board[si][sj] += (N + M)
        attack_turn[si][sj] = t
        fight_set = set()
        fight_set.add((si, sj))
        fight_set.add((ei, ej))

        # 레이저 공격
        if not bfs(N, M, board, si, sj, ei, ej):
            # 만약 레이저 공격에 실패한다면? -> 포탄
            bomb(N, M, board, si, sj, ei, ej)

        # 포탑 정비: 공격에 무관했던 포탑은 공격력이 1씩 올라간다.
        for i in range(N):
            for j in range(M):
                if board[i][j] > 0 and (i, j) not in fight_set:
                    board[i][j] += 1

        # 생존한 포탑 수 확인: 부서지지 않은 포탑이 1개가 된다면 그 즉시 중지
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] <= 0:
                    cnt += 1
        if cnt <= 1:
            break

    return max(map(max, board))

def main():
    # 입력들
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    attack_turn = [[0] * M for _ in range(N)]

    # K번의 톤이 돌아가는 simulate()함수
    print(simulate(N, M, K, board, attack_turn))

if __name__ == '__main__':
    main()