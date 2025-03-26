def place_tromino(depth, x, y):
    global max_val, curr, n, m, visited, directions

    if depth == 3:
        tmp = curr[:]
        max_val = max(max_val, sum(tmp))
        return
    
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            curr.append(grid[next_x][next_y])
            visited[next_x][next_y] = True

            place_tromino(depth + 1, next_x, next_y)
            curr.pop()
            visited[next_x][next_y] = False


def main():
    global max_val, grid, curr, n, m, visited, directions
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    max_val = 0
    visited = [[False] * m for _ in range(n)]
    curr = []
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                place_tromino(0, i, j)

    print(max_val)

if __name__ == '__main__':
    main()