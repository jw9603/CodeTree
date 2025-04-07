# 도로는 0, 도로가 아닌 곳은 1
# 메두사는 집에서 공원까지 산책을 나가기로 함
# 메두사는 오직 도로만을 따라 최단 경로로 공원까지 이동


# M명의 전사들이 메두사를 잡기 위해 마을에 도착
# 각 전사는 초기에 (ri, ci)에 위치해 있으며, 메두사를 향한 최단 경로로 이동함
# 전사는 도로와 비도로를 구분하지 않고 어느 칸이든 이동가능

# 전사들이 마을에 들어와있음을 미리 알고 있던 메두사는 전사들이 움직이기 전에 그들을 바라봄으로써 돌로 만들어 
# 움직임을 멈출 수 있다.


# 메두사와 전사들의 이동은 매턴마다 다음 순서에 맞춰 차례로 진행된다.

# 1. 메두사의 이동

    # 메두사는 도로를 따라 한 칸 이동하며, 공원까지 최단 경로를 따릅니다. 
    # 메두사가 이동한 칸에 전사가 있을 경우 전사는 메두사에게 공격을 받고 사라짐
    # 만약 집으로부터 공원까지 여러 최단경로가 가능하다면 상, 하, 좌, 우의 우선순위를 따름.
    # 메두사의 집으로부터 공원까지 도달하는 경로가 없을수도 있다.

    # 즉, 한 칸 이동 -> 이동한 칸에 전사 유뮤 확인

# 2. 메두사의 시선

    #  매두사는 상, 하, 좌, 우 하나의 방향을 선택해 바라봄
    # 메두사는 바라보는 방향으로 90도의 시야각을 가짐
    # 메두사의 시야각 안에 들어와있지만 다른 전사에 가려진 전사의 경우 메두사에게 보이지 않는다.

    # 특정 전사에 의해 메두사에게 가려지는 범위는 메두사와 해당 전사의 상대적인 위치에 의해 결정됨.
    # 상하좌우 대각선 8방향을 나누었을 때, 메두사로부터 8방향 중 한 방향에 전사가 위치해 있다면, 그 전사가
    # 동일한 방향으로 바라본 범위에 포함된 모든 칸은 메두사에게 보이지 않음

    # 메두사가 본 전사들은 모두 돌로 변해 현재 턴에는 움직일 수 없으며, 이번 턴이 종료되었을 때 돌에서 풀려남
    # 전사는 한 칸에 여려명 있을수 있음

    # 메두사는 상, 하, 좌, 우 중 전사를 가장 많이 볼 수 있는 방향을 바라봄

    # 즉, 메두사는 상, 하, 좌, 우 중 전사를 가장 많이 볼 수 잇는 방향을 바라보며, 전사들은 전사들에게 가려져서 살 수 있다.
    # 또한, 메두사가 본 전사들은 한 턴간 움직일 수 없으며, 턴이 끝나면 움직일 수 있음

# 3. 전사들의 이동

    # 돌로 변하지 않은 전사들은 메두사를 향해 최대 두 칸까지 이동. (전사들은 메두사를 향해 최단 경로로 이동중)

    # 아래는 이 두 칸을 어떻게 이동하는지,,!

        # 1. 첫 번째 이동
            # 메두사와 거리를 줄일 수 있는 방향으로 한 칸 이동. 이런 방향이 두 개 이상일 경우 상, 하, 좌, 우의 우선순위로 방향을 선택
            # 격자의 바깥을 나갈 수 없으며, 메두사의 시야에는 ㄴㄴ -> 이것이 BFS의 범위 조건에 들어갈 것
        
        # 2. 두 번째 이동
            # 메두사와 거리를 줄일 수 있는 방향으로 한 칸 더 이동. 이런 방향이 두 개 이상일 경우 좌, 우, 상, 하의 우선순위로 방향을 선택한다.
            # 격자의 바깥을 나갈 수 없으며, 메두사의 시야에 들어오는 곳으로는 이동 X

# 4. 전사의 공격
    # 메두사와 같은 칸에 도달 -> 공격
    # 그러나 메두사가 너무 강한 나머지 이기지 못하고 사라짐

# 위의 네 단계에서 최단경로는 맨해틑 거리를 기준으로 계산

# 위의 네 단계가 반복되어 메두사가 공원에 도달할 때 까지 매 턴마다 해당 턴에서 모든 전사가 이동한 거리의 합,
# 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수를 공백을 사이에 두고 출력하는 프로그램 작성
# 단, 메두사가 공원에 도착하는 턴에는 0을 출력하고 프로그램 종료

# 입 출력

# 입력:
    # 마을의 크기 N, 전사의 수 M이 공백을 사이에 두고
    # 다음 줄에 메두사의 집의 위치 정보 sr, sc와 공원의 위치 정보 er, ec
    # 다음 줄에 M명의 전사들의 좌표가 주어짐
    # 다음 줄부터 N줄에 거쳐 마을의 도로 정보가 주어짐

# 출력:
    # 각 턴마다 한 불에 모든 전사가 이동한 거리의 합, 메두사로 인해 돌이 된 전사의 수, 메두사를 공격한 전사의 수를 공백을 사이에 두고 출력
    # 단, 메두사가 공원에 도착하는 턴에는 0을 출력하고 프로그램 종료
    # 만약, 메두사의 집으로부터 공원까지 이어지는 도로가 존재하지 않는다면 -1을 출력

from collections import deque
# 방향 우선순위
DRC = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
DRC_SECOND = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌우상하

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def find_route(si, sj, ei, ej):
    queue = deque()
    prev = [[0]*N for _ in range(N)]

    queue.append((si, sj))
    prev[si][sj] = (si, sj)
    while queue:
        ci, cj = queue.popleft()

        if (ci, cj) == (ei, ej):
            path = []
            ci, cj = prev[ci][cj]

            while (ci, cj) != (si, sj):
                path.append((ci, cj))
                ci, cj = prev[ci][cj]
            return path[::-1]

        for d in DRC:

            ni, nj = ci + d[0], cj + d[1]

            if 0 <= ni < N and 0 <= nj < N and prev[ni][nj] == 0 and board[ni][nj] == 0:
                prev[ni][nj] = (ci, cj)
                queue.append((ni, nj))
    return -1

def mark_line(v, ci, cj, dr):

    while 0 <= ci < N and 0 <= cj < N:

        v[ci][cj] = 2
        ci, cj = ci + di[dr], cj + dj[dr]

def mark_safe(v, si, sj, dr, org_dr):

    ci, cj = si + di[dr], sj + dj[dr]
    mark_line(v, ci, cj, dr)
    ci, cj = si + di[org_dr], sj + dj[org_dr]

    while 0 <= ci < N and 0 <= cj < N:

        mark_line(v, ci, cj, dr)
        ci, cj = ci + di[org_dr], cj + dj[org_dr]

def make_stone(marr, mi, mj, dr):

    v = [[0] * N for _ in range(N)]

    cnt = 0
    ni, nj = mi + di[dr], mj + dj[dr]

    while 0 <= ni < N and 0 <= nj < N:

        v[ni][nj] = 1
        if marr[ni][nj] > 0:
            cnt += marr[ni][nj]
            ni, nj = ni + di[dr], nj + dj[dr]
            mark_line(v, ni, nj, dr)
            break

        ni, nj = ni + di[dr], nj + dj[dr]

    for org_dr in ((dr - 1) % 8, (dr + 1) % 8):

        si, sj = mi + di[org_dr], mj + dj[org_dr]

        while 0 <= si < N and 0 <= sj < N:
            if v[si][sj] == 0 and marr[si][sj] > 0:
                v[si][sj] = 1
                cnt += marr[si][sj]
                mark_safe(v, si, sj, dr, org_dr)
                break
            ci, cj = si, sj

            while 0 <= ci < N and 0 <= cj < N:
                if v[ci][cj] == 0:
                    v[ci][cj] = 1
                    if marr[ci][cj] > 0:
                        cnt += marr[ci][cj]
                        mark_safe(v, ci, cj, dr, org_dr)
                        break
                else:
                    break
                ci, cj = ci + di[dr], cj + dj[dr]
            si, sj = si + di[org_dr], sj + dj[org_dr]

    return v, cnt

def move_warriors(v, mi, mj):

    move, attk = 0, 0

    for dirs in [DRC, DRC_SECOND]:
        for idx in range(len(warriors)-1, -1, -1):
            ci, cj = warriors[idx]
            if v[ci][cj] == 1:
                continue
            dist = abs(mi - ci) + abs(mj - cj)
            for d in dirs:
                ni, nj = ci + d[0], cj + d[1]
                if 0 <= ni < N and 0 <= nj < N and v[ni][nj] != 1 and dist > abs(mi - ni) + abs(mj - nj):
                    if (ni, nj) == (mi, mj):
                        attk += 1
                        warriors.pop(idx)
                    else:
                        warriors[idx] = [ni, nj]
                    move += 1
                    break
    return move, attk

def main():
    global N, warriors, board
    N, M = map(int, input().split())
    si, sj, ei, ej = map(int, input().split())
    warriors_input = list(map(int, input().split()))
    warriors = [[warriors_input[i], warriors_input[i+1]] for i in range(0, M*2, 2)]
    board = [list(map(int, input().split())) for _ in range(N)]

    route = find_route(si, sj, ei, ej)
    if route == -1:
        print(-1)
    else:
        for mi, mj in route:
            for i in range(len(warriors)-1, -1, -1):
                if warriors[i] == [mi, mj]:
                    warriors.pop(i)
            marr = [[0]*N for _ in range(N)]
            for ti, tj in warriors:
                marr[ti][tj] += 1
            mx_stone = -1
            v = []
            for dr in (0, 4, 6, 2):
                tv, tstone = make_stone(marr, mi, mj, dr)
                if mx_stone < tstone:
                    mx_stone = tstone
                    v = tv
            move_cnt, attk_cnt = move_warriors(v, mi, mj)
            print(move_cnt, mx_stone, attk_cnt)
        print(0)

if __name__ == '__main__':
    main()