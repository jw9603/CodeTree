def spread_dust(n, m, room):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tmp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if room[i][j] > 0:
                spread_amount = room[i][j] // 5
                cnt = 0
                for dx, dy in direction:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and room[ni][nj] != -1:
                        tmp[ni][nj] += spread_amount
                        cnt += 1

                room[i][j] -= spread_amount * cnt
    
    for i in range(n):
        for j in range(m):
            room[i][j] += tmp[i][j]

def operate_air_cleaner(n, m, room, cleaner):
    direction1 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    direction2 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 위쪽 - 반시계
    x, y = cleaner[0], 0
    d = 0
    tmp = 0

    while True:
        nx, ny = x + direction1[d][0], y + direction1[d][1]

        if 0 <= nx < n and 0 <= ny < m:
            if room[nx][ny] != -1:
                room[nx][ny], tmp = tmp, room[nx][ny]

                x, y = nx, ny

            else:
                break
        else:
            d += 1
    
    # 아래쪽 - 시계
    x, y = cleaner[1], 0
    d = 0
    tmp = 0

    while True:
        nx, ny = x + direction2[d][0], y + direction2[d][1]

        if 0 <= nx < n and 0 <= ny < m:
            if room[nx][ny] != -1:
                room[nx][ny], tmp = tmp, room[nx][ny]

                x, y = nx, ny

            else:
                break
        else:
            d += 1
    
def simulate(n, m, t, room, cleaner):

    for _ in range(t):
        spread_dust(n, m, room)
        operate_air_cleaner(n, m, room, cleaner)
    
    total = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] > 0:
                total += room[i][j]
    
    return total

def main():
    n, m, t = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]

    cleaner = []
    for i in range(n):
        if room[i][0] == -1:
            cleaner.append(i)
    
    print(simulate(n, m, t, room, cleaner))

if __name__ == '__main__':
    main()