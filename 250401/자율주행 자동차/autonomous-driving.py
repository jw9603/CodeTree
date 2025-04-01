def count_car_roads(n, m, x, y, d, grid):
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    cnt = 1

    while True:
        found = False

        for _ in range(4):
            d = (d + 3) % 4
            next_x, next_y = x + dx[d], y + dy[d]

            if 0 <= next_x < n and 0 <= next_y < m:
                if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    cnt += 1
                    x, y = next_x, next_y
                    found = True
                    break
        if not found:
            next_x, next_y = x - dx[d], y - dy[d]
            if 0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] == 0:
                x, y = next_x, next_y
            else:
                return cnt

def main():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(count_car_roads(n, m, x, y, d, grid))

if __name__ == '__main__':
    main()