############################################# 문제 이해  #############################################
# 1번부터 P번까지 P명의 산타

# 1. 게임판의 구성
# 게임판은 N * N 크기의 격자로 이루어져 있다. 각 위치는 (r, c)의 형태로 표현되며, 좌상단은 (1, 1)
# 게임은 총 M개의 턴에 걸쳐 진행
    # 매 턴마다 루돌프와 산타들이 한 번씩 움직인다.
    # 1. 루돌프가 한 번 움직이고
    # 2. 1번부터 P번 산타까지 순서대로 움직이게 된다.
    # 이때 기절해있거나 격자 밖으로 빠져나가 게임에 탈락한 산타들은 움직일 수 없다.


# 2. 루돌프의 움직임
# 루돌프는 가장 가까운 산타를 향해 1칸 돌진. 단 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 선택!
# 만약 가장 가까운 산타가 2명 이상이라면, r 좌표가 큰 산타를 향해 돌진, r이 동일할 경우, c좌표가 큰 산타를 향해 돌진
# 루돌프는 8방향 중 하나로 돌진 가능,

# 루돌프는 8방향 기준 가장 가까운 산타를 향해 1칸 돌진

# 3. 산타의 움직음
# 1번부터 P번까지 순서대로 움직임
# 기절했거나 탈락한 산타는 움직일 수 없다.
# 산타는 루돌프에게 가장 거리가 가까워지는 방향으로 1칸 (상우하좌)
# 움직일 수 있는 칸이 없다면 움직이지 않는다.
# 움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않는다.

# 4. 충돌
# 산타와 루돌프가 같은 칸에 있게 되면 충돌이 발생

# 루돌프가 움직여서 산타 있는곳으로 가서 충돌이 나면, 해당 한타는 C만큼의 점수를 얻게된다.
# 이와 동시에 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀려나게 된다.

# 산타가 움직여서 충돌이 일어난 경우, 해당 산타는 D만큼의 점수를 얻게 된다.
# 이와 동시에 산타는 자신이 이동해온 반대방향으로 D만큼 밀려나게 된다.

# 만약 밀려난 위치가 게임판 밖이라면 산타는 게임에서 탈락
# 만약 밀려난 칸에 다른 산타가 있는 경우 상호작용이 발생

# 5. 상호작용
# 루돌프와 충돌 후 산타는 포물선의 궤적으로 이동하여 착지하게 되는 칸에서만 상호작용 발생
# 포물선의 궤적이라는 것은 밀려나면서 다른 것들을 건드리지 않는다는 뜻
# 산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 방향으로 밀려나게 된다.
# 그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려난다. -> 이것도 마찬가지로 게임판 밖으로 밀려나오게 된 산타의 경우
# 게임에서 탈락

# 6. 기절
# 산타는 루돌프와 충돌 후 기절하게 된다.
# 현재가 K번째 턴이었다면, K + 1번째 턴까지 기절하게 되어 (K + 2)번째 턴부터 다시 정상상태가 된다.
# 기절한 산타는 움직일 수 없다. 단, 기절한 도중 충돌이나 상호작용으로 인해 밀려날 수는 있다.
# 루돌프는 기절한 산타를 돌진 대상으로 선택할 수 있다.

# 7. 게임 종료
# M 번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임이 종료된다.
# 만약 P 명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임이 종료된다.
# 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여

# 게임이 끝났을 때 각 산타가 얻은 최종 점수를 구하는 프로그램을 짜라

############################################# 문제 이해  #############################################

############################################# 알고리즘  #############################################
# 입력
# 첫 번째 줄에 N, M(게임 턴 수), P(산타의 수), C(루돌프의 힘), D(산타의 힘)가 주어짐
# 다음 줄에는 루돌프의 초기 위치 (R_r, R_c)가 주어진다.
# 다음 P개의 줄에 걸쳐서 산타의 번호 P_n과 초기 위치 (S_r, S_c)가 주어짐.

# 출력
# 게임이 끝났을 때 각 산타가 얻은 최종 점수를 1번부터 P번까지 순서대로 공백을 사이에 두고 출력한다.

# 산타는 1번부터 P번까지 순서대로 주어지고, 죽었냐, 살았냐를 표기하는 flag 자료형도 필요하다.
# 순차적인 표기 -> 리스트, flag -> 리스트
############################################# 알고리즘  #############################################
# from collections import deque
# def move_santa(idx, si, sj, rdi, rdj, C, N, santa, alive, board):
#     '''
#     루돌프가 산타가 있는곳으로 와서 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀려나게 된다.
#     산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면 그 산타는 1칸 해당 뱡향으로 밀려나게 된다.
#     그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복하게 된다.

#     '''
#     queue = deque([(idx, si, sj, C)])

#     while queue:
#         cur_santa, cur_i, cur_j, cur_c = queue.popleft()

#         next_i, next_j = cur_i + rdi * cur_c, cur_j + rdj * cur_c

#         if 0 <= next_i < N and 0 <= next_j < N:
#             if board[next_i][next_j] == 0:
#                 board[next_i][next_j] = cur_santa
#                 santa[cur_santa] = [next_i, next_j]
#                 return
#             # 날라간 산타위치에 이미 산타가 있을 경우
#             else:
#                 queue.append((board[next_i][next_j], next_i, next_j, 1))
#                 board[next_i][next_j] = cur_santa
#                 santa[cur_santa] = [next_i, next_j]
#         else: # 게임판 밖으로 밀려나게 되었으니 산타 탈락
#             alive[cur_santa] = 0
#             return

# def rodulpe_move(P, C, N, turn, santa, ri, rj, board, alive, scores, wakeup_turn):
#     '''
#     루돌프는 가장 가까운 산타를 향해 1칸 돌진
#     단, 게임에서 탈락하지 않은 산타 중 가장 가까운 산타를 선택
#     가장 가까운 산타가 2명 이상이라면, r 좌표가 큰 산타, c좌표가 큰 산타
#     '''
#     min_dist = float('inf')
#     target_santa = []

#     for p in range(1, P + 1):
#         if not alive[p]:
#             continue

#         si, sj = santa[p]
#         dist = (ri - si) ** 2 + (rj - sj) ** 2
        
#         if dist < min_dist:
#             min_dist = dist
#             target_santa = [(si, sj, p)]
#         elif dist == min_dist:
#             target_santa.append((si, sj, p))
    
#     target_santa.sort(reverse=True)

#     # 현재 루돌프로부터 가장 가까운 산타의 정보
#     si, sj, idx = target_santa[0]

#     # 루돌프의 방향 설정
#     if ri > si:
#         rdi = -1
#     elif ri < si:
#         rdi = 1
#     else:
#         rdi = 0
    
#     if rj > sj:
#         rdj = -1
#     elif rj < sj:
#         rdj = 1
#     else:
#         rdj = 0
    
#     # 루돌프의 한 칸 이동
#     board[ri][rj] = 0
#     ri += rdi
#     rj += rdj
#     board[ri][rj] = -1

#     # 충돌 (이건 루돌프가 산타가 있는곳으로 온 경우)
#     if (ri, rj) == (si, sj):
#         scores[idx] += C
#         wakeup_turn[idx] = turn + 2
#         move_santa(idx, si, sj, rdi, rdj, C, N, santa, alive, board)
    
#     return ri, rj

# def santa_move(N, P, D, ri, rj, board, turn, santa, scores, alive, wakeup_turn):
#     '''
#     산타는 1번부터 P번까지 순서대로 움직인다.
#     루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
#     산타는 다른 산타가 있는 칸이나 게임판 밖으로는 움직일 수 없다 <- 이동시 조건
#     움직일 수 있는 칸이 없다면 산타는 움직이지 않는다.
#     산타는 상우하좌 우선순위에 맞춰 움직입니다.
#     '''
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     for p in range(1, P + 1):
#         if not alive[p] or wakeup_turn[p] > turn:
#             continue
        
#         si, sj = santa[p]

#         # 루돌프에게 거리가 가장 가까워지는 방향으로 1칸
#         min_dist = (ri -si) ** 2 + (rj - sj) ** 2
#         next_move = None

#         # 이 반복문에서 가장 가까운 거리로 갈 수 있는 위치를 update
#         for di, dj in directions:
#             next_i, next_j = si + di, sj + dj

#             if 0 <= next_i < N and 0 <= next_j < N and board[next_i][next_j] <= 0:
#                 dist = (ri - next_i) ** 2 + (rj - next_j) ** 2
#                 if dist < min_dist:
#                     min_dist = dist
#                     next_move = (next_i, next_j, di, dj)
        
#         # 움직일 수 있는 칸이 없다면 산타는 움직이지 않는다.
#         if not next_move:
#             continue
        
#         ni, nj, di, dj = next_move
        
#         # 충돌: 이번에는 산타가 루돌프가 있는곳으로 이동하여 발생하는 충돌
#         if (ri, rj) == (ni, nj):
#             scores[p] += D
#             wakeup_turn[p] = turn + 2
#             board[si][sj] = 0
#             move_santa(p, ni, nj, -di, -dj, D, N, santa, alive, board)
#         else:
#             board[si][sj] = 0
#             board[ni][nj] = p
#             santa[p] = [ni, nj]

# def all_eliminated(alive):
#     return sum(alive[1:]) == 0

# def play_turn(N, M, P, C, D, board, ri, rj, santa, alive, scores, wakeup_turn):

#     for turn in range(1, M + 1):
#         if all_eliminated(alive):
#             break
        
#         # 1. 루돌프 움직임
#         ri, rj = rodulpe_move(P, C, N, turn, santa, ri, rj, board, alive, scores, wakeup_turn)

#         # 2. 산타가 1번부터 P번까지 순서대로 움직임
#         santa_move(N, P, D, ri, rj, board, turn, santa, scores, alive, wakeup_turn)

#         # 2. 산타가 1번부터 P번까지 살아 있냐? -> 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여
#         for p in range(1, P + 1):
#             if alive[p]:
#                 scores[p] += 1

# from collections import deque

# def main():
#     N, M, P, C ,D = map(int, input().split())
#     board = [[0] * N for _ in range(N)]

#     ri, rj = map(lambda x: int(x) - 1, input().split()) # 루돌프의 초기 위치
#     board[ri][rj] = -1 # 루돌프

#     scores = [0] * (P + 1) # 각 산타가 얻은 최종 점수
#     alive = [0] + [1] * P # 산타의 생존 여부 flag
    
#     santa = [[0] * 2 for _ in range(P + 1)]
#     wakeup_turn = [1] * (P + 1)

#     for _ in range(P):
#         idx, si, sj = map(int, input().split())
#         santa[idx] = [si - 1, sj - 1]
#         board[si - 1][sj - 1] = idx
    
#     # 매턴마다 돌리는 함수
#     play_turn(N, M, P, C, D, board, ri, rj, santa, alive, scores, wakeup_turn)
    
#     print(*scores[1:])

# if __name__ == '__main__':
#     main()

# from collections import deque
# def move_santa(santa_idx, si, sj, rdi, rdj, C, N, santa, alive, board):
#     '''
#     이 함수는 루돌프에 의해 산타가 밀려나는 것을 구현한 함수
#     루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 루돌프가 이동해온 방향으로 C 칸 밀려나게 됨

#     여기서 상호작용도 발생
#     산타가 날라가게 되어 도착하는 위치에 만약 산타가 있다면 상호작용 발생
#     상호작용은 그 위치에 있는 산타가 날라온 방향으로 1칸 밀려나는 것, 
#     밀려난 곳에 또 산타가 있다면 그 산타도 1칸 밀려나감.
#     이 부분은 deque로 구현이 필요하다는 것을 알 수 잇음
#     '''
#     queue = deque([(santa_idx, si, sj, C)])

#     while queue:
#         cur_santa, cur_i, cur_j, cur_c = queue.popleft()

#         next_i, next_j = cur_i + rdi * cur_c, cur_j + rdj * cur_c

#         if 0 <= next_i < N and 0 <= next_j < N:
#             if board[next_i][next_j] == 0:
#                 board[next_i][next_j] = cur_santa
#                 santa[cur_santa] = [next_i, next_j]
#                 return
#             else:
#                 queue.append((board[next_i][next_j], next_i, next_j, 1))
#                 board[next_i][next_j] = cur_santa
#                 santa[cur_santa] = [next_i, next_j]
            
#         else:
#             alive[cur_santa] = 0
#             return


# def move_rodulpe(N, P, C, ri, rj, board, turn, scores, alive, santa, wakeup_turn):
#     '''
#     루돌프는 가장 가까운 산타를 향해 1칸 돌진, 단 게임에서 탈락하지 않은(alive) 산타
#     8방향
#     '''
    
#     # 1. 일단 최소 거리를 찾는다.
#     min_dist = float('inf')
#     target_santa = []

#     for p in range(1, P + 1):
#         if not alive[p]:
#             continue

#         si, sj = santa[p]
#         dist = (ri - si) ** 2 + (rj - sj) ** 2

#         if dist < min_dist:
#             min_dist = dist
#             target_santa = [(si, sj, p)]
#         elif dist == min_dist:
#             target_santa.append((si, sj, p))
    
#     # 2. target_santa에 들어있는 것들이 여러 개라면 우선순위를 정해야 함
#     # 2명 이상이라면, r좌표가 큰 산타를 향해 돌진, r이 동일한 경우, c좌표가 큰 산타를 향해 돌진
#     target_santa.sort(reverse=True)

#     # 3. 가장 가까운 산타 발견
#     si, sj, santa_idx = target_santa[0]

#     # 4. 루돌프의 방향 설정: 루돌프 좌표(ri, rj), 산타 좌표(si, sj)
#     if ri > si:
#         rdi = -1
#     elif ri < si:
#         rdi = 1
#     else:
#         rdi = 0
    
#     if rj > sj:
#         rdj = -1
#     elif rj < sj:
#         rdj = 1
#     else:
#         rdj = 0
    
#     # 5. 이제 루돌프가 움직여야게찌?
#     board[ri][rj] = 0
#     ri += rdi
#     rj += rdj
#     board[ri][rj] = -1

#     # 6. 루돌프가 움직여서 충돌이 일어난 경우
#     # 해당 산타는 C만큼의 점수를 얻게 된다. 
#     # 이와 동시에 산타는 루돌프가 이동해온 방향으로 C칸 만큼 밀려나게 된다

#     if (ri, rj) == (si, sj):
#         scores[santa_idx] += C
#         wakeup_turn[santa_idx] = turn + 2
#         move_santa(santa_idx, si, sj, rdi, rdj, C, N, santa, alive, board)
    
#     return ri, rj

# def santa_move(N, P, D, ri, rj, board, santa, scores,turn, alive, wakeup_turn):
#     '''
#     산타는 1번부터 P번까지 순서대로 움직인다.
#     기절했거나 이미 게임에 탈락한 산타다? -> 움직이지 못한다. (continue로 넘기기)
#     산타는 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
#     움직일 수 있는 칸이 없다면 산타는 움직이지 않는다. -> 이것도 변수를 만들어서 표시해야하는구나
#     ㅇ
#     '''
#     directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#     for p in range(1, P + 1):
#         if not alive[p] or wakeup_turn[p] > turn:
#             continue
#         si, sj = santa[p]

#         # 루돌프는 1마리, 현재 p산타와의 거리 측정 바로 가능
#         min_dist = (ri - si) ** 2 + (rj - sj) ** 2
#         # 움직일 수 있는 칸을 표시
#         next_move = None

#         # 이 과정을 통해 상, 우, 하, 좌 의 방향 중 가장 가까워질 방향과 한 칸 이동 좌표를 구한다.
#         for di, dj in directions:
#             next_i, next_j = si + di, sj + dj

#             if 0 <= next_i < N and 0 <= next_j < N and board[next_i][next_j] <= 0:
#                 # 실제 거리
#                 dist = (next_i - ri) ** 2 + (next_j - rj) ** 2
#                 if dist < min_dist:
#                     min_dist = dist
#                     next_move = (next_i, next_j, di, dj)
        
#         if not next_move:
#             continue

#         ni, nj, di, dj = next_move

#         # 충돌할 경우: 이 경우는 산타가 움직여서 루돌프가 있는곳으로 온 경우
#         if (ni, nj) == (ri, rj):
#             scores[p] += D
#             wakeup_turn[p] = turn + 2
#             board[si][sj] = 0
#             # 산타는 자신이 이동해온 반대 방향으로 D칸 만큼 밀려나게 됨
#             move_santa(p, ni, nj, -di, -dj, D, N, santa, alive, board)   
#         else:
#             board[si][sj] = 0
#             board[ni][nj] = p
#             santa[p] = [ni, nj]
    

# def all_eliminated(alive):
#     return sum(alive[1:]) == 0

# def play_turn(N, M, P, C, D, board, ri, rj, santa, alive, scores, wakeup_turn):

#     for turn in range(1, M + 1):
#         # 만약 P명의 산타가 모두 게임에서 탈락하게 된다면 그 즉시 게임 종료
#         if all_eliminated(alive):
#             break

#         # 1. 루돌프의 움직임
#         ri, rj = move_rodulpe(N, P, C, ri, rj, board, turn, scores, alive, santa, wakeup_turn)

#         # 2. 산타가 1번 부터 P번까지 순서대로 움직임
#         # 아래 코드에서 1번부터 P번까지 반복
#         santa_move(N, P, D, ri, rj, board, santa, scores,turn, alive, wakeup_turn)


#         # 3. 매 턴 이후 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여
#         for p in range(1, P + 1):
#             if alive[p]:
#                 scores[p] += 1
    



# def main():
#     N, M, P, C, D = map(int, input().split())

#     # 루돌프의 초기 위치
#     ri, rj = map(lambda x: int(x) - 1, input().split())

#     # 게임판의 구성: 1마리의 루돌프: -1, 빈 칸: 0, 1번부터 P번까지의 산타
#     board = [[0] * N for _ in range(N)]
#     board[ri][rj] = -1
    
#     # 결과 저장 리스트: 1번부터 P번까지의 산타가 얻은 최종 점수
#     scores = [0] * (P + 1)

    
#     # 산타 관련 데이터
#     # 1. 산타의 좌표: 산타 번호에 해당하는 산타의 x, y 좌표
#     # 2. 산타의 생존 여부: 1은 생존, 0은 죽음
#     # 3. 산타 기절 여부
#     santa = [[0] * 2 for _ in range(P + 1)]
#     alive = [0] + [1] * P
#     wakeup_turn = [1] * (P + 1)

#     # P 개의 줄에 걸쳐 산타의 번호와 초기 위치(si, sj)가 주어진다.
#     for _ in range(P):
#         idx, si, sj = map(int, input().split())
#         santa[idx] = [si - 1, sj - 1]
#         board[si - 1][sj - 1] = idx
    
#     # M 번의 턴에 걸쳐 수행
#     play_turn(N, M, P, C, D, board, ri, rj, santa, alive, scores, wakeup_turn)

#     print(*scores[1:])

# if __name__ == '__main__':
#     main()

# 루돌프의 반란

# M 번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 이후 게임이 종료
# 루돌프가 움직이고, 1번부터 P번까지의 산타가 순서대로 움직인다.
# 매 턴 이후 아직 탈락하지 않은 산타들이게는 1점씩을 추가로 부여

# 원하는 결과: 게임이 끝났을 때 각 산타가 얻은 최종 점수를 구해라

from collections import deque
def move_rodulpe(N, P, C, ri, rj, turn, board, santa, alive, scores, wakeup_turn):
    '''
    루돌프는 가장 가까운 산타를 향해 1칸 돌진
    '''

    min_dist = float('inf')
    target_santa = []

    for p in range(1, P + 1):
        if not alive[p]:
            continue

        si, sj = santa[p]
        dist = (si -ri) ** 2 + (sj - rj) ** 2

        if dist < min_dist:
            min_dist = dist
            target_santa = [(si, sj, p)]
        elif dist == min_dist:
            target_santa.append((si, sj, p))
    
    target_santa.sort(reverse=True)

    si, sj, santa_idx = target_santa[0]

    # 가장 가까운 산타를 골랐으니 이제 루돌프가 한 칸 움직일 방향을 구해야 한다.
    if ri < si:
        rdi = 1
    elif ri > si:
        rdi = -1
    else:
        rdi = 0
    
    if rj < sj:
        rdj = 1
    elif rj > sj:
        rdj = -1
    else:
        rdj = 0
    
    # 이제 루돌프가 움직여야게찌?
    board[ri][rj] = 0
    ri += rdi
    rj += rdj
    board[ri][rj] = -1


    # 루돌프가 움직여서 충돌이 난 경우
    if (ri, rj) == (si, sj):
        scores[santa_idx] += C
        wakeup_turn[santa_idx] = turn + 2
        move_santa(santa_idx, si, sj, rdi, rdj, C, N, santa, alive, board)
    
    return ri, rj

def move_santa(santa_idx, si, sj, rdi, rdj, C, N, santa, alive, board):
    '''
    이 코드는 산타가 날라가서, 착지 후 상호작용까지 구현하는 코드
    
    '''
    queue = deque([(santa_idx, si, sj, C)])

    while queue:
        cur_santa, cur_i, cur_j, cur_c = queue.popleft()

        ni, nj = cur_i + rdi * cur_c, cur_j + rdj * cur_c

        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] == 0:
                board[ni][nj] = cur_santa
                santa[cur_santa] = [ni, nj]
                return
            else:
                queue.append((board[ni][nj],ni,nj, 1))
                board[ni][nj] = cur_santa
                santa[cur_santa] = [ni, nj]

        else:
            alive[cur_santa] = 0
            return

def santa_move(N, P, D, turn, ri, rj, scores, santa, board, alive, wakeup_turn):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for p in range(1, P + 1):
        if not alive[p] or wakeup_turn[p] > turn: 
            continue
        si, sj = santa[p]

        min_dist = (ri - si) ** 2 + (rj - sj) ** 2
        # 움직일 수 있는 칸이 없다면 산타는 움직이지 않는다.
        # 움직일 수 있는 칸이 있더라도 만약 루돌프로부터 가까워질 수 있는 방법이 없다면 산타는 움직이지 않는다.
        next_move = None 
        for di, dj in directions:
            ni, nj = si + di, sj + dj

            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] <= 0:
                dist = (ni - ri) ** 2 + (nj - rj) ** 2
                if dist < min_dist:
                    min_dist = dist
                    next_move = (ni, nj, di, dj)
        
        if not next_move:
            continue

        ni, nj, di, dj = next_move

        # 충돌할 경우
        if (ni, nj) == (ri, rj):
            scores[p] += D
            wakeup_turn[p] = turn + 2
            board[si][sj] = 0
            move_santa(p, ni, nj, -di, -dj, D, N, santa, alive, board)
        else:
            board[si][sj] = 0
            board[ni][nj] = p
            santa[p] = [ni, nj]


def all_eliminated(alive):
    return sum(alive[1:]) == 0

def play_turn(N, M, P, C, D, ri, rj, board, santa, scores, alive, wakeup_turn):
    '''
    M번의 턴동안 루돌프의 움직임 -> 1번, 2번 ,... , P번의 산타 움직임 -> 탈락하지 않은 산타 점수 += 1

    '''

    for turn in range(1, M + 1):
        # 만약 모든 산타가 탈락했다면?
        if all_eliminated(alive):
            break
        # 1. 루돌프의 움직임: 이를 통해 루돌프가 움직인 결과 좌표를 받아야 한다.
        ri, rj = move_rodulpe(N, P, C, ri, rj, turn, board, santa, alive, scores, wakeup_turn)

        # 2. 산타의 움직인
        santa_move(N, P, D, turn, ri, rj, scores, santa, board, alive, wakeup_turn)

        # 3. 탈락하지 않은 산타들 점수 += 1
        for p in range(1, P + 1):
            if alive[p]:
                scores[p] += 1
        

def main():
    N, M, P, C, D = map(int, input().split())

    # 루돌프의 초기 위치
    ri, rj = map(lambda x: int(x) - 1, input().split())

    # 게임판의 구성: 이 게임판에 값들은 산타 번호, 루돌프 번호(-1)
    board = [[0] * N for _ in range(N)]
    board[ri][rj] = -1


    scores = [0] * (1 + P)
    alive = [0] + [1] * P
    santa = [[0] * 2 for _ in range(P + 1)]
    wakeup_turn = [1] * (P + 1)

    for _ in range(P):
        idx, si, sj = map(int, input().split())
        santa[idx] = [si - 1, sj - 1]
        board[si - 1][sj - 1] = idx

    # M번의 턴
    play_turn(N, M, P, C, D, ri, rj, board, santa, scores, alive, wakeup_turn)

    print(*scores[1:])

if __name__ == '__main__':
    main()