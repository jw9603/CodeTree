######################################## 문제 이해 ########################################
# 정령들이 R행 C열의 격자 형태로 이루어진 마법의 숲을 탐색하려고 한다.
# 가장 위를 1행, 가장 아래를 R행으로 한다.

# 숲의 동, 서, 남은 마법의 벽으로 막혀 있으며, 정령들은 숲의 북쪽을 통해서만 숲에 들어올 수 있다.

# 총 K명의 정령은 각자 골렘을 타고 숲을 탐색합니다.
# 각 골렘은 십자 모양의 구조를 가지고 있으며, 중앙 칸을 포함해 총 5칸을 차지합니다.

# 골렘의 중앙을 제외한 4칸 중 한 칸은 골렘의 출구
# 정령은 어떤 방향에서든 골렘에 탑승할 수 있지만 
# 골렘에서 내릴 때에는 정해진 출구를 통해서만 내릴 수 있다.

# i번째로 숲을 탐색하는 골렘은 숲의 가장 북쪽에서 시작해 골렘의 중앙이 ci열이 되도록 하는 위치에서 내려오기 시작
# 초기 골렘의 출구는 d_i의 방향에 위치해 있다.

# 골렘은 숲을 탐색하기 위해 다음과 같은 우선순위로 이동한다. 더 이상 움직이지 못할 때까지 해당 과정을 반복한다.

# 1. 남쪽으로 한 칸 내려간다. (가능할 떄 까지만)
# 2. 1의 방법으로 이동할 수 없으면 서쪽 방향으로 회전?하면서 내려간다. (출구는 반시계방향ㅇ으로 이동)
# 3. (1)과 (2)의 방법으로 이동할 수 없으면 동쪽 방향으로 회전하면서 내려간다. (출구는 시계방향으로 이동)

# 골렘이 이동할 수 있는 가장 남쪽에 도달해 더이상 이동할 수 없으면 정령은 골렘 내에서 상하좌우 인접한 칸으로 이동이 가능하다.
# 단, 만약 현재 위치하고 있는 골렘의 출구가 다른 골렘과 인접하고 있다면 해당 출구를 통해 다른 골렘으로 이동 가능

# 정령은 갈 수 있는 모든 칸 중 가장 남쪽의 칸으로 이동하고 완전히 종료한다.
# 이때 정령의 위치가 해당 정령의 최종 위치가 된다.

# 정령의 최종 위치의 행번호의 합을 구해야 하기에 각 정령이 도달하게 되는 최종 위치를 누적해야 합니다.

# 만약 골렘이 최대한 남쪽으로 이동했지만 골렘의 몸 일부가 여전히 숲을 벗어난 상태라면,
# 해당 골렘을 포함해 숲에 위치한 모든 골렘들은 숲을 빠져나간 뒤 다음 골렘부터 새롭게 숲의 탐색을 시작
# 단, 이 경우에는 정령이 도달하는 최종 위치를 답에 포함시키지 않는다.
######################################## 문제 이해 ########################################
######################################## 알고리즘 빌드 업 #######################################
# 입력
# 숲의 크기 (R, C), 정령의 수 K가 주어진다.
# 그 다음 줄부터 K개의 줄에 거쳐 각 골렘이 출발하는 열 ci, 골렘의 출구 방향 정보 di가 공백을 두고 주어진다.
# di는 북(0), 동(1), 남(2), 서(3)

# 출력
# 첫번째 줄에 각 정령들이 최종적으로 위치한 행의 총합을 출력
######################################## 알고리즘 빌드 업 #######################################
from collections import deque

def can_place_south(board, ci, cj):
    return board[ci + 1][cj - 1]  == 0 and board[ci + 2][cj] == 0 and board[ci + 1][cj + 1] == 0

def can_place_west(board, ci, cj):
    return (
        board[ci - 1][cj - 1] == 0 and board[ci][cj - 2] == 0 
        and board[ci + 1][cj - 1] == 0 and board[ci + 1][cj - 2] == 0 
        and board[ci + 2][cj - 1] == 0
    )

def can_place_east(board, ci, cj):
    return (
        board[ci - 1][cj + 1] == 0 and board[ci][cj + 2] == 0 and board[ci + 1][cj + 1] == 0
        and board[ci + 1][cj + 2] == 0 and board[ci + 2][cj + 1] == 0
    )

def place_golem(board, ci, cj, golem_num):
    '''
    (ci, cj) == 정령, 즉 골렘의 중심
    '''
    board[ci + 1][cj] = board[ci - 1][cj] = golem_num
    board[ci][cj - 1] = board[ci][cj] = board[ci][cj + 1] = golem_num


def bfs(R, C, board, exit_set, start_i, start_j):
    '''
    골렘위에 탑승한 정령이 도달할 수 있는 가장 남쪽칸
    
    정령은 골렘 내에서 상하좌우 인접한 칸으로 이동이 가능합니다.
    단, 만약 현재 위치하고 있는 골렘의 출구가 다른 골렘과 인접!!! 하고 있다면 해당 출구를 통해 다른 골렘으로 이동 가능
    '''
    global dx, dy
    queue = deque([(start_i, start_j)])
    visited = [[0] * (C + 2) for _ in range(R + 4)]
    visited[start_i][start_j] = 1
    max_row = 0
    while queue:
        cur_i, cur_j = queue.popleft()
        max_row = max(max_row, cur_i)

        for d in range(4):
            next_i, next_j = cur_i + dx[d], cur_j + dy[d]

            if visited[next_i][next_j]:
                continue
            if board[next_i][next_j] == board[cur_i][cur_j]:
                visited[next_i][next_j] = 1
                queue.append((next_i, next_j))  
            elif (cur_i, cur_j) in exit_set and board[next_i][next_j] > 1:
                visited[next_i][next_j] = 1
                queue.append((next_i, next_j))

    return max_row - 2  

def main():
    global dx, dy
    R, C, K = map(int, input().split()) # R행 C열
    golem = [list(map(int, input().split())) for _ in range(K)]


    # 동, 남, 서에 벽(1) 추가
    board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C + 2)] 
    exit_set = set() 
    ans = 0
    golem_num = 2

    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    
    for cj, dr in golem:
        # i번째로 숲을 탐색하는 골렘은 숲의 가장 북쪽에서 시작해 골렘의 중앙이 ci열이 되도록 하는 위치에서 내려오기 시작
        # 초기 골렘의 출구는 d_i의 방향에 위치해 있다.

        ci = 1 # 중앙
        
        while True:
            if can_place_south(board, ci, cj):
                ci += 1
            elif can_place_west(board, ci, cj):
                ci += 1
                cj -= 1
                dr = (dr - 1) % 4
            elif can_place_east(board, ci ,cj):
                ci += 1
                cj += 1
                dr = (dr + 1) % 4
            else:
                break
        
        # 골렘이 최대한 남쪽으로 이동햇지만 골렘의 몸 일부가 여전히 숲을 벗어난 상태라면
        # 해당 골렘을 포함한 모든 골렘은 사라지고 맵이 초기화 된다.
        # 아직 못들어왔다는겨
        if ci < 4:
            board = [[1] + [0] * C + [1] for _ in range(R+3)] + [[1] * (C + 2)] 
            exit_set = set()
            golem_num = 2
        else:
            place_golem(board, ci, cj, golem_num)
            # 이제 배치를 완료햇으면 정령이 이동할 수 있는 위치로 가는 계산을 해야 함
            golem_exit_pos = (ci + dx[dr], cj + dy[dr])
            exit_set.add(golem_exit_pos)
            ans += bfs(R, C, board,exit_set, ci, cj) # 행의 좌표를 추가
            golem_num += 1

    print(ans)

if __name__ == '__main__':
    main()
