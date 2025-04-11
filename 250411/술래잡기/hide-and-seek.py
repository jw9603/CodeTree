###################################### 문제 이해 ######################################
# 술래잡기 게임은 n * n 크기의 격자에서 진행되며 술래는 처음 정중앙에 서있다.
# m명의 도망자가 있다.
# 도망자는 처음 지정된 곳에 서있다.
# 도망자는 중앙에서 시작하지 않는다. 
# 도망자의 종류는 좌우로만 움직이는 유형과 상하로만 움직이는 유형이 있다.
# 좌우로만 움직이는 사람은 항상 오른쪽을 보고 시작
# 상하로만 움직이는 사람은 항상 아래쪽을 보고 시작

# 이 게임에는 h개의 나무가 있다.
# 나무가 도망자와 초기에 겹쳐져 주어지는것 가능하다.

# 술래잡기 게임에서는 m명의 도망자가 먼저 동시에 움직이고, 그 다음 술래가 움직인다.
# 이렇게 도망자가 1턴 그리고 술래가 1턴 진행하는 것을 총 K번 반복하게 된다.

# 이때 도망자가 움직일 때 현재 술래와의 거리가 3 이하인 도망자만 움직인다.
# 술래와의 거리가 3 이하인 도망자들은 1턴 동안 다음 규칙에 따라 움직이게 된다.

# 현재 바라보고 있는 방향으로 1칸 움직인다 햇을때 격자를 벗어나지 않는 경우
    # 움직이려는 칸에 술래가 있는 경우라면 움직이지 않는다.
    # 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동한다. 해당 칸에 나무가 있어도 괜찮다.

# 현재 바라보고 있는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
    # 먼저 방향을 반대로 틀어준다. 이후 바라보고 있는 방향으로 1칸 움직인다 햇을 때 해당 위치에 술래가 없다면 1칸 앞으로 이동


# k번에 걸쳐 술래잡기를 진행하는 동안 술래가 총 얻게된 점수를 출력하는 프로그램을 작성
###################################### 문제 이해 ######################################
###################################### 알고리즘 ######################################
# 입력
# 첫 번째 줄에 n, m, h, k가 주어진다.
# 이후 m개의 줄에 걸쳐 도망자의 위치 (x, y)와 이동 방법 d가 공백을 사이에 두고 차례대로 주어진다.
# 이동 방법 d가 1인 경우 좌우, 2인 경우 상하로만 움직임을 뜻한다.
# 또한, 좌우로 움직이는 사람은 항상 오른쪽을 보고 시작하며, 상하로 움직이는 사람은 항상 아래쪽을 보고 시작
# 이후 h개의 줄에 걸쳐 나무의 위치 x, y가 공백을 사이에 두고 차례대로 주어진다.

# 출력
# 술래가 K번의 턴 동안 얻게되는 총 점수를 출력



###################################### 알고리즘 ######################################
# def simulate(N, M, H, K, runners, trees):

#     # 좌, 우, 하, 상
#     di = [0, 0, 1, -1]
#     dj = [-1, 1, 0, 0]

#     # 반대 방향
#     opp = {0: 1, 1: 0, 2: 3, 3: 2}
    
#     # 술래의 방향: 상, 우, 하, 좌
#     tdi = [-1, 0, 1, 0]
#     tdj = [0, 1, 0, -1]

#     # 술래의 초기 위치
#     ti, tj, td = N // 2, N // 2, 0

#     # 달팽이 코드 초기 변수들
#     max_cnt = 1 # 현재 방향으로 이동할 최대 횟수 (달팽이 꺾을 타이밍 결정)
#     cnt = 0     # 현재 방향으로 이동한 횟수
#     flag = 0    # 방향 전환 시 한 번은 유지하고, 두 번째에서 max_cnt 증가시킴
#     val = 1     # 방향 회전의 진행 방향 (1이면 시계 방향, -1이면 반시계 방향)

#     ans = 0
#     # K턴의 게임 진행
#     for k in range(1, K + 1):
#         # 1. 도망자들의 이동
#         for i in range(len(runners)):
#             # 1.1 도망자가 움직일 때 현재 술래와의 거리가 3이하인 도망자만 움직인다.
#             if abs(runners[i][0] - ti) + abs(runners[i][1] - tj) <= 3:
#                 ni, nj = runners[i][0] + di[runners[i][2]], runners[i][1] + dj[runners[i][2]]

#                 # 1.1.1 움직이려는 칸에 술래가 있지 않다면 해당 칸으로 이동한다. 해당 칸에 나무가 있어도 괜찮다.
#                 if 0 <= ni < N and 0 <= nj < N and (ni, nj) != (ti, tj):
#                     runners[i][0], runners[i][1] = ni, nj

#                 else: # 1.2 현재 바라보고 잇는 방향으로 1칸 움직인다 했을 때 격자를 벗어나는 경우
#                     runners[i][2] = opp[runners[i][2]]

#                     # 이후 바라보고 있는 방향으로 1칸 움직인다. 해당 위치에 술래가 없다면
#                     ni, nj = runners[i][0] + di[runners[i][2]], runners[i][1] + dj[runners[i][2]]

#                     if (ni, nj) != (ti, tj):
#                         runners[i][0], runners[i][1] = ni, nj

#         # 2. 술래 이동: 달팽이 이동
#         cnt += 1
#         ti, tj = ti + tdi[td], tj + tdj[td]

#         if (ti, tj) == (0, 0): # 안쪽 달팽이 종료
#             max_cnt, cnt, flag, val = N, 1, 1, -1
#             td = 2
        
#         elif (ti, tj) == (N // 2, N // 2): # 바깥 달팽이 종료
#             max_cnt, cnt, flag, val = 1, 0, 0, 1
#             td = 0

#         # 평소에는 cnt를 증가시키며 max_cnt와 비교
#         else:
#             if cnt == max_cnt: # 방향 꺾는 시점
#                 cnt = 0
#                 td = (td + val) % 4 # 방향 회전 (val로 시계/반시계 결정)
#                 if flag == 0:
#                     flag = 1
#                 else:
#                     flag = 0
#                     max_cnt += val  # 두 번에 한 번만 max_cnt 증가
        


#         # 3. 도망자 잡기: 술래자리 포함 3칸
#         tset = set(((ti, tj), (ti + tdi[td], tj + tdj[td]), (ti + tdi[td] * 2, tj + tdj[td] * 2)))
        
#         for i in range(len(runners) - 1, -1, -1):
#             rx, ry = runners[i][0], runners[i][1]
#             if (rx, ry) in tset and (rx, ry) not in trees:
#                 runners.pop(i)
#                 ans += k
        
#         # 도망자가 없다면 더이상 점수도 없음
#         if not runners:
#             break
    
#     return ans


# def main():
#     N, M, H, K = map(int, input().split())

#     # m개의 줄에 걸쳐 도망자의 위치 (x, y)와 이동 방법 d가 주어진다.
#     runners = []
#     for _ in range(M):
#         i, j, d = map(int, input().split()) # d:1 좌우, d:2상하
#         runners.append([i - 1, j - 1, d])
    
#     # h개의 줄에 걸쳐 나무의 위치 (x, y), 나무는 이동하지도 않고 겹치지도 않기 때문에 집합으로 두자
#     trees = set()
#     for _ in range(H):
#         x, y = map(lambda x: int(x) - 1, input().split())
#         trees.add((x, y))

#     print(simulate(N, M, H, K, runners, trees))

# if __name__ == '__main__':
#     main()



def simulate(N, M, H, K, arr, tree):
    # 방향 정의
    di, dj = [0, 0, 1, -1], [-1, 1, 0, 0]  # 도망자 이동
    tdi, tdj = [-1, 0, 1, 0], [0, 1, 0, -1]  # 술래 달팽이 방향
    opp = {0: 1, 1: 0, 2: 3, 3: 2}

    mid = (N + 1) // 2
    ti, tj, td = mid, mid, 0  # 술래 시작 위치 및 방향
    mx_cnt, cnt, flag, val = 1, 0, 0, 1  # 달팽이 회전 변수
    ans = 0

    for k in range(1, K + 1):
        # 1. 도망자 이동
        for i in range(len(arr)):
            if abs(arr[i][0] - ti) + abs(arr[i][1] - tj) <= 3:
                ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
                if 1 <= ni <= N and 1 <= nj <= N and (ni, nj) != (ti, tj):
                    arr[i][0], arr[i][1] = ni, nj
                else:
                    arr[i][2] = opp[arr[i][2]]
                    ni, nj = arr[i][0] + di[arr[i][2]], arr[i][1] + dj[arr[i][2]]
                    if 1 <= ni <= N and 1 <= nj <= N and (ni, nj) != (ti, tj):
                        arr[i][0], arr[i][1] = ni, nj

        # 2. 술래 이동
        cnt += 1
        ti, tj = ti + tdi[td], tj + tdj[td]
        if (ti, tj) == (1, 1):
            mx_cnt, cnt, flag, val = N, 1, 1, -1
            td = 2
        elif (ti, tj) == (mid, mid):
            mx_cnt, cnt, flag, val = 1, 0, 0, 1
            td = 0
        elif cnt == mx_cnt:
            cnt = 0
            td = (td + val) % 4
            flag = 1 - flag
            if flag == 0:
                mx_cnt += val

        # 3. 도망자 잡기
        tset = set()
        for d in range(3):
            ni, nj = ti + tdi[td] * d, tj + tdj[td] * d
            if 1 <= ni <= N and 1 <= nj <= N:
                tset.add((ni, nj))

        for i in range(len(arr) - 1, -1, -1):
            if (arr[i][0], arr[i][1]) in tset and (arr[i][0], arr[i][1]) not in tree:
                arr.pop(i)
                ans += k

        if not arr:
            break

    return ans


def main():
    N, M, H, K = map(int, input().split())

    # 도망자 정보: (x, y, d)
    arr = []
    for _ in range(M):
        x, y, d = map(int, input().split())
        arr.append([x, y, d])  # d: 0(좌), 1(우), 2(하), 3(상)

    # 나무 좌표 집합
    tree = set()
    for _ in range(H):
        i, j = map(int, input().split())
        tree.add((i, j))

    print(simulate(N, M, H, K, arr, tree))


if __name__ == '__main__':
    main()
