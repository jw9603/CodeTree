# 그림은 n x n 크기의 격자
# 각 칸의 색깔을 1이상 10이하의 숫자로 표현

# 예술 점수는 모든 그룹 쌍의 조화로움의 합으로 정의된다.
# 그룹 a와 그룹 b의 조화로움은 == (그룹 a에 속한 칸의 수 + 그룹 b에 속한 칸의 수) * 그룹 a를 이르고 있는 숫자 값 * 그룹 b를 이루고 있는 숫자 값
# * 그룹 a와 그룹 b가 서로 맛닿아 있는 변의 수로 정의
# # 초기 예술 점수, 1회전 이후 예술 점수, 2회전 이후 예술 점수, 그리고 3회전 이후 예술 점수의 합을 구해라

############################################## 알고리즘 ##############################################
# 입력
# 첫 번째 줄에 n이 주어진다. n은 무조건 홀수
# 이후 n개의 줄에 걸쳐 각 행에 칠해져 있는 색깔에 대한 정보인 숫잘들이 공백을 사이에두고 주어진다.



############################################## 알고리즘 ##############################################
from collections import deque, defaultdict
def bfs(n, board, si, sj, visited, group_id, groups, values):
    queue = deque([(si, sj)])
    visited[si][sj] = group_id
    groups[group_id] = [(si, sj)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    values[group_id] = board[si][sj]

    while queue:
        ci, cj = queue.popleft()

        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] == -1 and board[ni][nj] == board[si][sj]:
                visited[ni][nj] = group_id
                groups[group_id].append((ni, nj))
                queue.append((ni, nj))

def compute_groups(n, board):
    visited = [[-1] * n for _ in range(n)]
    group_id = 0
    # key: 그룹 번호, value: 좌표
    groups = defaultdict(list)

    # key: 그룹 번호, value:값
    values = defaultdict(int)

    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(n, board, i, j, visited, group_id, groups, values)
                group_id += 1

    
    return groups, values

def compute_scores(n, groups, values):
    '''
    그룹간의 조화로움 계산
    '''
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    group_ids = list(groups.keys())
    score = 0
    for i in range(len(group_ids)):
        for j in range(i + 1, len(group_ids)):
            g1, g2 = group_ids[i], group_ids[j]

            val = 0

            for x1, y1 in groups[g1]:
                for dx, dy in directions:
                    nx, ny = x1 + dx, y1 + dy
                    if (nx, ny) in groups[g2]:
                        val += 1
            score += (len(groups[g1]) + len(groups[g2])) * values[g1] * values[g2] * val
    
    return score
 
def rotate(n, board):
    m = n // 2
    new_board = [row[:] for row in board]
    left_right = [(0, 0), (0, m + 1), (m + 1, 0), (m + 1, m + 1)]


    # 십자 회전: 반 시계 방향으로 
    for i in range(n):
        new_board[m][i] = board[i][m]
        new_board[i][m] = board[m][n - 1 - i]

    # 4개의 정사각형: 시계 방향으로 회전
    for sx, sy in left_right:
        for i in range(m):
            for j in range(m):
                new_board[sx + i][sy + j] = board[sx + m - 1 - j][sy + i]
    
    return new_board

def simulate(n, board):
    total_score = 0

    for _ in range(4):
        # 1. 그룹을 나눈다.
        groups, values = compute_groups(n, board)
        # 2. 나누어진 그룹에서 조하로움의 합을 계산한다.
        total_score += compute_scores(n, groups, values)
        # 3. 회전한다.
        board = rotate(n, board)
    
    return total_score

def main():
    n = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(simulate(n, board))

if __name__ == '__main__':
    main()
