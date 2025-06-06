# 유적지는 5 x 5 격자 형태로 되어 있으며, 각 칸에는 다양한 유물의 조각이 배치되어 있다.
# 유물의 조각은 총 7가지 종류로, 1 ~ 7

# 1. 탐사 진행

# 3 x 3 격자 선택

# 5 x 5 격자 내에서 3 x 3 격자를 선택하여 격자를 회전시킬 수 있다.
# 선택된 격자는 시계 방향으로 90도, 180, 270도 중 하나의 각도만큼 회전시킬 수 있다.
# 선택된 격자는 항상 회전을 진행해야만 한다.

# 회전 목표

# 가능한 회전의 방법 중 
# 1. 유물 1차 획득 가치를 최대화하고, 그러한 방법이 여러가지인 경우
# 2. 회전한 각도가 가장 작은 방법을 선택
# 3. 그러한 경우도 여러가지인 경우
# 4. 회전 중심 좌표의 열이 가장 작은 구간을, 그리고 열이 같다면 행이 가장 작은 구간을 선택


# 2. 유물 획득

# 2.1 유물 1차 획득

# 상하좌우로 인접한 같은 종류의 유물 조각은 서로 연결되어 있다.
# 이 조각들이 3개 이상 연결된 경우, 조각이 모여 유물이 되고 사라진다.
# 유물의 가치는 모인 조각의 개수

# 유적의 벽면에는 1부터 7사이의 숫자가 M개 적혀있다. 
# 이들은 유적에서 조각이 사라졌을 때 새로 생겨나는 조각에 대한 정보를 담고 있다.

# 조각이 사라진 위치에는 유적의 벽면에 적혀있는 순서대로 새로운 조각이 생겨납니다.
# 새로운 조각은 
# 1. 열 번호가 작은 순으로 
# 2. 열 번호가 같다면 행 번호가 큰 순

# 2.2 유물 연쇄 획득

# 새로운 유물 조각이 생겨난 이후에도 조각들이 3개 이상 연결될 수 있습니다.
# 앞과 같은 방식으로 조각이 모여 유물이 되고 사라진다.
# 사라진 위치에는 또 다시 새로운 조각이 생겨나며 
# 이는 더 이상 조각이 3개 이상 연결되지 않아 유물이 될 수 없을때 까지 반복

# 3. 탐사 반복
# 탐사 진행 ~ 유물 연쇄 획득의 과정까지를 1턴으로 생각
# 총 K번의 턴에 걸쳐 진행

# 각 턴마다 획득한 유물의 가치의 총합을 출력
# 단, 아직 K번의 턴을 진행하지 못했지만, 탐사 진행 과정에서 어떠한 방법을 사용하더라도 유물을 획득할 수 없다면 종료
# 이 경우 얻을 수 있는 유물이 존재하지 않음으로, 종료되는 턴에 아무 값도 출력하지 않음


################################# 문제 빌드업 #################################

# 입력
# 첫 번째 줄에 탐사의 반복 횟수 K와 벽면에 적힌 유물 조각의 개수 M이 공백을 사이에 두고 주어짐
# 5개의 줄에 걸쳐 유물의 각 행에 있는 유물 조각에 적혀 있는 숫자들이 공백을 두고 주어짐
# 그 다음 줄에는 벽면에 적힌 M개의 유물 조각 번호가 공백을 사이에 두고 순서대로 주어짐

# 출력
# 첫 번째 줄에 각 턴 마다 획득한 유물의 가치의 총합을 공백을 두고  출력

# 알고리즘

# 1. 탐사 진행 (K 번)
# for _ in range(K):
    # 90: 1, 180: 2, 270: 3
    # for turn_time in range(1, 4) # 회전수의 우선 순위:  열 -> 행
        # for x in range(3)  # 3 * 3 행렬이니까
            # for y in range(3):
                # turn_time만큼 90도 회전
                # for _ in range(turn_time)
                    # rotate()
                
                # 유물 개수 카운드
                # 유물 최대 개수 업데이트 -> 이것을 하는 이유는 최대가 되는 회전이 몇도인
    
    # 유물이 없는 경우 즉시 종료

    # 2. 연쇄 획득
    # while True:

# ################################ 문제 빌드업 #################################
# from collections import deque

# def rotate(grid, i, j):
#     new_grid = [row[:] for row in grid]

#     for x in range(3):
#         for y in range(3):
#             new_grid[i + x][j + y] = grid[i + 3 - y - 1][j + x] # 

#     return new_grid


# def bfs(grid, visited, i, j, flag):
#     cnt = 0
#     queue = deque([(i, j)])
#     visited[i][j] = True
#     connected = set()
#     connected.add((i, j))

#     value = grid[i][j] # 탐색을 시작하는 값과 같은지 체크하기 위해 필요
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     while queue:
#         r, c = queue.popleft()
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and grid[nr][nc] == value:
#                 visited[nr][nc] = True
#                 queue.append((nr, nc))
#                 connected.add((nr, nc))

#     if len(connected) >= 3:
#         if flag == 1:
#             for i, j in connected:
#                 grid[i][j] = 0
#         return len(connected)
#     else:
#         return 0

# def count_and_remove(grid, flag):

#     '''
#     같은 종류의 유물 조각이 3개 이상인 연결된 경우를 찾아 제거하고, 제거된 조각의 수를 반환
#     조각의 수는 유물의 가치임   
#     '''
    
#     visited = [[False] * 5 for _ in range(5)]
#     total = 0
#     removed = []

#     for i in range(5):
#         for j in range(5):
#             if not visited[i][j] and grid[i][j] != 0:

#                 total += bfs(grid, visited, i, j, flag)
    
#     return total

# def simulate(grid, nums, K):
#     results = []

#     for _ in range(K):  # K턴을 진행 (유물 획득을 못하면 즉시 종료)
#         best = (-1, 0, 0, 0, [])  # (유물 수, 회전 횟수, 열, 행, 회전 결과)

#         for rot in range(1, 4):  # 1회, 2회, 3회 회전 (90, 180, 270)
#             for j in range(3):
#                 for i in range(3):
#                     temp = [row[:] for row in grid] 

#                     for _ in range(rot):
#                         temp = rotate(temp, i, j)

#                     cnt = count_and_remove(temp, 0)
                    
#                     # 가능한 회전의 방법 중 유물 1차 획득 가치를 최대화 하고,
#                     # 그러한 방법이 여러가지인 경우 회전한 각도가 가장 작은 방법
#                     # 그러한 경우도 여러가지인 경우 회전 중심 좌표가 열이 가장 작은 구간, 이것도 같으면 행
#                     if cnt > best[0] or (cnt == best[0] and (rot, j, i) < (best[1], best[2], best[3])):
#                         best = (cnt, rot, j, i, temp)

#         if best[0] == 0:
#             break  # 유물 못얻으면 종료
        
#         # 2. 유물 연쇄 획득
#         grid = [row[:] for row in best[4]] # 현재 상태에서 가장 유물을 얻기 좋은 grid
#         total_gain = 0

#         while True:
#             cnt = count_and_remove(grid, 1)
#             if cnt == 0: # 유물이 없으면 정지
#                 break

#             total_gain += cnt

#             for j in range(5):
#                 for i in range(4, -1, -1):
#                     if grid[i][j] == 0 and nums:
#                         grid[i][j] = nums.popleft()

#         results.append(total_gain)
    
#     print(*results)

# def main():
#     K, M = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(5)]

#     nums = deque(map(int, input().split()))
#     simulate(grid, nums, K)

# if __name__ == "__main__":
#     main()

# 고대 문명 유적 탐사
# 이 유적지는 5 x 5 격자 형태
# 각 칸에는 다양한 유물의 조각이 배치되어 있다.
# 유물 조각은 7가지 종류: 1 ~ 7

# 탐사진행 -> 유물 획득 -> 유물 연쇄 획득의 과정을 1턴
# 총 K번의 턴에 걸쳐 진행

# 각 턴마다 획득한 유물의 가치의 총합을 출력하는 프로그램 작성
# 단, 아직 K번의 턴을 진행하지 못했지만, 탐사 진행 과정에서 어떠한 방법을
# 사용하더라도 유물을 획득할 수 없었다면 모든 탐사는 그 즉시 종료.

# 1. 탐사 진행
# 3 x 3 격자 선택을 한다. 이 격자를 선택하고 회전을 해야한다.
# 회전은 시계방향으로 90, 180, 270도가 있는데, 이 3가지 중 선택하는 조건이 있다.
# 유물 1차 획득 가치를 최대화 -> 회전한 각도가 가증 작은 방법 -> 
# 회전 중심 좌표의 열이 가장 작은 구간 -> 행이 가장 작은 구간

# 2. 유물 획득

# 2.1 유물 1차 획득
#
# def rotate(grid, i, j):
#     new_grid = [row[:] for row in grid]

#     for x in range(3):
#         for y in range(3):
#             new_grid[i + x][j + y] = grid[i + 3 - y - 1][j + x]
    
#     return new_grid

# def bfs(grid, visited, i, j, flag):
#     cnt = 0
#     queue = deque([(i, j)])
#     visited[i][j] = True
#     connected = set()
#     connected.add((i, j))

#     value = grid[i][j]
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     while queue:
#         r, c = queue.popleft()
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#             if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc] and grid[nr][nc] == value:
#                 visited[nr][nc] = True
#                 queue.append((nr, nc))
#                 connected.add((nr, nc))
    
#     if len(connected) >= 3:
#         if flag == 1:
#             for i, j in connected:
#                 grid[i][j] = 0
#         return len(connected)
#     else:
#         return 0

# def count_and_remove(grid, flag):
#     '''
#     같은 종류의 유물 조각이 3개 이상이 연결된 경우를 찾아 제거하고, 제거된 조각의 수를 반환
#     조각의 수는 유물의 가치
#     '''
#     visited = [[False] * 5 for _ in range(5)]
#     total = 0

#     for i in range(5):
#         for j in range(5):
#             if not visited[i][j] and grid[i][j] != 0:
#                 total += bfs(grid, visited, i, j, flag)
    
#     return total

# from collections import deque
# def simulate(grid, walls, K):
#     results = []
#     # K턴을 진행 ()
#     # 아직 K번의 턴을 진행하지 못했지만, 탐사 진행 과정에서 어떠한 방법을
#     # 사용하더라도 유물을 획득할 수 없었다면 모든 탐사는 그 즉시 종료.
#     for _ in range(K):
#         best = (-1, 0, 0, 0, []) # 유물 수, 회전 횟수, 열, 행, 회전 결과
#         for rot in range(1, 4):
#             for j in range(3):
#                 for i in range(3):
#                     temp = [row[:] for row in grid]

#                     for _ in range(rot):
#                         temp = rotate(temp, i, j)
                    
#                     cnt = count_and_remove(temp, 0)

#                     if cnt > best[0] or (cnt == best[0] and (rot, j, i) < (best[1], best[2], best[3])):
#                         best = (cnt, rot, j, i, temp)

        
#         if best[0] == 0:
#             break

#         # 2. 유물 연쇠 획득
#         grid = [row[:] for row in best[4]]
#         total_gain = 0

#         while True:
#             cnt = count_and_remove(grid, 1)
#             if cnt == 0:
#                 break

#             total_gain += cnt

#             for j in range(5):
#                 for i in range(4, -1, -1):
#                     if grid[i][j] == 0 and walls:
#                         grid[i][j] = walls.popleft()
            
#         results.append(total_gain)
    
#     print(*results)




# def main():
#     K, M = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(5)]

#     walls = deque(map(int, input().split()))
    
#     simulate(grid, walls, K)

# if __name__ == '__main__':
#     main()
from collections import deque
def rotate(grid, i, j):
    new_grid = [row[:] for row in grid]

    for x in range(3):
        for y in range(3):
            new_grid[i + x][j + y] = grid[i + 3 - y - 1][j + x]
    
    return new_grid

def count(grid, flag):

    visited = [[False] * 5 for _ in range(5)]
    total = 0

    for i in range(5):
        for j in range(5):
            if not visited[i][j] and grid[i][j] != 0:
                total += bfs(grid, i, j, flag, visited)

    return total

def bfs(grid, i, j, flag, visited):
    queue = deque([(i, j)])
    visited[i][j] = True
    value = grid[i][j]
    connected = set()
    connected.add((i, j))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        ci, cj = queue.popleft()
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj] and grid[ni][nj] == value:
                visited[ni][nj] = True
                queue.append((ni, nj))
                connected.add((ni, nj))
    
    if len(connected) >= 3:
        if flag == 1:
            for i, j in connected:
                grid[i][j] = 0
        return len(connected)
    else:
        return 0

def simulate(grid, walls, K):
    '''
    각 턴 마다 획득한 유물의 가치의 총합을 출력
    '''
    results = []

    for _ in range(K):

        # 1. 여기서 유물 1차 획득을 최대화 하는 회전 결과 리스트 찾음 = tmp==best[-1]
        best = (-1, 0, 0, 0, []) # 유물 수, 회전 횟수, 열, 행, 결과 리스트
        for rot in range(1, 4):
            for j in range(3):
                for i in range(3):
                    tmp = [row[:] for row in grid]

                    for _ in range(rot):
                        tmp = rotate(tmp, i, j)
                    
                    cnt = count(tmp, 0)

                    if cnt > best[0] or (cnt == best[0] and (rot, j, i) < (best[1], best[2], best[3])):
                        best = (cnt, rot, j, i, tmp)
        
        if best[0] == 0:
            break

        # 2. 유물 연쇄 획득
        grid = [row[:] for row in best[4]]
        total_gain = 0

        while True:
            cnt = count(grid, 1)
            if cnt == 0:
                break

            total_gain += cnt

            for j in range(5):
                for i in range(4, -1, -1):
                    if grid[i][j] == 0 and walls:
                        grid[i][j] = walls.popleft()
        results.append(total_gain)
    
    print(*results)

def main():
    K, M = map(int, input().split())
    # 5개의 줄에 걸쳐 유물의 각 행에 있는 유물 조각에 적혀 있는 숫자들이 주어짐
    grid = [list(map(int, input().split())) for _ in range(5)]

    walls = deque(map(int, input().split()))

    simulate(grid, walls, K)

if __name__ == '__main__':
    main()