####################################### 문제 이해 ####################################### 
# L X L 크기의 체스판 위에서 대결을 준비하고 있다.
# 체스판의 왼쪽 상단은 (1, 1)로 시작하며, 각 칸은 빈 칸 (0), 함정 (1), 벽 (2)으로 구성되어 있다.
# 체스판 밖도 벽으로 간주한다 ->> 이거 마법의 숲 탐색처럼 뭔가 벽을 처리 해야하는 느낌

# 왕실의 기사들은 자신의 마력으로 상대방을 밀쳐낼 수 있다
# 각 기사의 초기 위치는 (r, c)로 주어지며, 그들은 방패를 들고 있기 때문에 (r, c)를 좌측 상단으로 하며
# h x w 크기의 직사각형 형태를 띄고 있다. 각 기사의 체력은 k

# 1. 기사 이동
# 상하좌우 중 하나로 한 칸 이동할 수 있습니다.
# 이때 만약 이동하려는 위치에 다른 기사가 잇다면 그 기사도 함께 연쇄적으로 한 칸 밀려나게 된다.
# 그 옆에 또 기사가 있다면 연쇄적으로 한 칸씩 밀리게 된다.
# 만약 기사가 이동하려는 방향의 끝에 벽이 있다면 모든 기사는 이동할 수 없게 된다.
# 또, 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 된다.

# 2. 대결 대미지
# 명령을 받은 기사가 다른 기사를 밀치게 되면, 밀려난 기사들은 피해를 입게 된다.
# 이때 각 기사들은 해당 기사가 이동한 곳에서 w * h 직사각형 내에 놓여 있는 함정의 수만큼만 피해를 입게 된다.

# 각 기사마다 피해를 받은 만큼 체력이 깎이게 되며, 현재 체력 이상의 데미지를 받을 경우 기사는 체스판에서 사라지게 된다.
# 단, 명령을 받은 기사는 피해를 입지 않으며, 기사들은 모두 밀린 이후에 데미지를 입게 된다.
# 밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 그 기사는 피해를 전혀 입지 않게 된다.

# Q번에 걸쳐 왕의 명령이 주어졌을 때, Q번의 대결이 모두 끝난 후 생존한 기사들이 총 받은 데미지의 합을 출력
####################################### 문제 이해 ####################################### 
####################################### 알고리즘 ####################################### 
# 입력
# 첫 번째 줄에 L(체스판의 크기), N(기사의 수), Q(명령의 수)가 주어짐
# 다음 L개의 줄에 걸쳐서 L * L 크기의 체스판에 대한 정보가 주어짐
    # 0: 빈칸
    # 1: 함정
    # 2: 벽

# 다음 N개의 줄에 걸쳐서 초기 기사들의 정보가 주어짐.
# 이 정보는 (r, c, h, w, k) 순
# 기사의 처음 위치는 (r, c), 세로 길이가 h, 가로 길이가 w인 직사각형 형태를 띄고 있으며, 초기 체력이 k라는 것을 의미
# 입력은 1번 기사부터 N번 기사까지 순서대로 정보가 주어짐

# 다음 Q 개의 줄에 걸쳐 왕의 명령에 대한 정보가 주어짐.
# 이 정보는 (i, d) 형태로 주어지며 이는 i번 기사에게 방향 d로 한 칸 이동하라는 명령.
# i는 1이상 N 이하의 값을 갖으며, 이미 사라진 기사 번호가 주어질수도 있음에 유의
# d는 위(0), 오(1), 아(2), 왼(3)

# 출력
# Q개의 명령이 진행된 이후, 생존한 기사들이 총 받은 대미지의 합을 출력

####################################### 알고리즘 ####################################### 
# from collections import defaultdict, deque
# def push_knight(start, dr, info, board, N):
#     '''
#     왕에게 명령을 받은 기사는 한 칸 이동한다, 
#     연쇄적으로 밀릴 수 있으며, 벽이 있으면 전부 취소됨. -> 이렇기 때문에 queue를 써야 함
#     이동 후 각 기사들은 밀린 곳에 함정이 있으면 피해를 입고,
#     체력이 0이되면 사라짐
#     밀렸더라도 밀쳐진 위치에 함정이 전혀 없다면 그 기사는 피해를 전혀 입지 않게 됨.
#     '''
#     # 상우하좌
#     di = [-1, 0, 1, 0]
#     dj = [0, 1, 0, -1]
#     queue = deque([start]) # start: 미는애

#     # 누적 데미지, 기사들은 모두 밀린 이후에 데미지를 입게 된다.
#     damage = [0] * (N + 1) 
#     pushed_set = set([start])

#     while queue:
#         cur = queue.popleft()
#         ci, cj, h, w, k = info[cur]

#         ni, nj = ci + di[dr], cj + dj[dr]

#         # 이동 후 위치에 벽이나 함정이 있는지 체크
#         for i in range(ni, ni + h):
#             for j in range(nj, nj + w):
#                 if board[i][j] == 2: # 벽 -> 바로 종료
#                     return
#                 if board[i][j] == 1: # 함정
#                     damage[cur] += 1
        
#         # 이동 후 위치에 다른 기사가 있는지 체크
#         for idx in info:
#             if idx in pushed_set:
#                 continue
            
#             ti, tj, th, tw, _ = info[idx]

#             # 이동한 기사의 영역과 다른 기사의 영역이 사각형으로 겹치는지 판별하는 조건
#             # 이동한 기사의 세로, 가로 범위: [ni, ni + h - 1], [nj, nj + w - 1]
#             # 다른 기사의 세로, 가로 범위: [ti, ti + th - 1], [tj, tj + tw - 1]
#             if ni <= ti + th - 1 and ni + h - 1 >= ti and tj <= nj + w - 1 and nj <= tj + tw - 1:
#                 queue.append(idx)
#                 pushed_set.add(idx)
        
#     # 명령을 받은 기사는 데미지를 받지 않음
#     damage[start] = 0

#     # 이제 연쇄 밀림 처리 당하는 것들을 실제로 이동 처리
#     for idx in pushed_set:
#         si, sj, h, w, k = info[idx]
#         if k <= damage[idx]:
#             info.pop(idx)
#         else:
#             ni, nj = si + di[dr], sj + dj[dr]
#             info[idx] = [ni, nj, h, w, k - damage[idx]]


# def simulate(L, N, Q, board, init_k, info, commands):

#     total_damage = 0

#     for idx, dr in commands: # idx: 1번 ~ N번, dr : 방향
#         if idx in info: # 기사들의 정보: info
#             push_knight(idx, dr, info, board, N)

#     for idx in info:
#         total_damage += init_k[idx] - info[idx][4]    
    
#     return total_damage

# def main():
    
#     L, N, Q = map(int, input().split())
#     board = [[2] * (L + 2)] # 구현

#     for _ in range(L):
#         row = list(map(int, input().split())) # 체스판
#         board.append([2] + row + [2]) # 벽
#     board.append([2] * (L + 2)) # 맨 밑줄에 벽 22 

#     # 각 기사들의 체력 저장 데이터
#     init_k = [0] * (N + 1)  # 리스트로 하냐? -> 
#     # 기사들의 정보: 계속 업데이트되는 정보 -> 
#     info = defaultdict(list)  # 키 1~ N 번호, 

#     # N개의 줄에 걸쳐서 초기 기사들의 정보가 주어짐
#     for n in range(1, N + 1):
#         r, c, h, w, k = map(int, input().split())
#         info[n] = [r, c, h, w, k]
#         init_k[n] = k

#     # Q개의 왕의 명령: (i, d) 형태로 주어짐
#     commands = [tuple(map(int, input().split())) for _ in range(Q)]

#     results = simulate(L, N, Q, board, init_k, info, commands)

#     print(results)

# if __name__ == '__main__':
#     main()

from collections import deque, defaultdict
def push_knight(start, dr, info, board, N):
    # 상, 우, 하, 좌
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    queue = deque([start])

    # 데미지 계산
    # 마지막 줄에서 데미지를 받은 만큼 info 자료에 업데이트하기 위해 필요한 자료형
    damage = [0] * (N + 1)

    # 밀리는 것들
    pushed_set = set([start])

    while queue:
        cur = queue.popleft()
        ci, cj, h, w, k = info[cur]

        # 한 칸 이동
        ni, nj = ci + di[dr], cj + dj[dr]

        # 이동 반경에 벽이나 함정이 있는지 확인
        # 벽일경우 바로 스탑, 함정이 있다면 함정 개수만큼 데미지 계산
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                if board[i][j] == 2:
                    return
                if board[i][j] == 1:
                    damage[cur] += 1
        
        for idx in info:
            if idx in pushed_set:
                continue
                
            ti, tj, th, tw, _ = info[idx]

            # 이동한 기사의 영역과 다른 기사 영역이 사각형으로 겹치는지
            # 이동한 기사의 세로: [ni, ni + h - 1]
            # 이동한 기사의 가로: [nj, nj + w - 1]
            if ni <= ti + th - 1 and ni + h - 1 >= ti and tj <= nj + w - 1 and tj + tw - 1 >= nj:
                queue.append(idx)
                pushed_set.add(idx)
    
    damage[start] = 0

    # 다 밀렸으니 이제 계산
    for idx in pushed_set:
       si, sj, h, w, k = info[idx]

       if k <= damage[idx]:
           info.pop(idx)
       else:
           ni, nj = si + di[dr], sj + dj[dr]
           info[idx] = [ni, nj, h, w, k - damage[idx]]

def simulate(L, N, Q, board, init_k, info, command):
    total_damage = 0

    for idx, dr in command:
        # 예외 조건2: 체스판에서 사라진 기사에게 명령을 내리면 아무런 반응이 없게 된다.
        if idx in info:
            push_knight(idx, dr, info, board, N)
    

    for idx in info:
        total_damage += init_k[idx] - info[idx][4]
    
    return total_damage

def main():
    L, N, Q = map(int, input().split())

    # 체스판 밖도 벽으로 간주한다. -> 아! 가장자리에 벽도 만들어야 겠구나!
    # 0: 빈 칸, 1: 함정, 2: 벽
    board = [[2] * (L + 2)]
    for _ in range(L):
        row = list(map(int, input().split()))
        board.append([2] + row + [2])
    board.append([2] * (L + 2))

    # 기사들은 맞짱을 다 까고, 밀린 이후에 대미지를 계산해야 한다.
    # 그렇다는 것은 남은 데미지 == 초기 체력 - 맞짱 데미지
    init_k = [0] * (N + 1)

    # 다음 N 개의 줄에 걸쳐서 초기 기사들의 정보가 주어진다.
    # 이것도 각 기사들마다의 정보를 저장하기 위해 defaultdict(list)
    info = defaultdict(list)
    for n in range(1, N + 1):
        r, c, h, w, k = map(int, input().split())
        info[n] = [r, c, h, w, k]
        init_k[n] = k
    
    # Q 개의 줄에 걸쳐 왕의 명령 (i, d)
    commands = [tuple(map(int, input().split())) for _ in range(Q)]

    print(simulate(L, N, Q, board, init_k, info, commands))

if __name__ == '__main__':
    main()