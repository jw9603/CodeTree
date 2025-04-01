def check_t_shape(x, y):
    global max_sum, t_shape, n, m, grid

    for shape in t_shape:
        total = grid[x][y]
        valid = True

        for dx, dy in shape:
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < n and 0 <= next_y < m:
                total += grid[next_x][next_y]
            else:
                valid = False
                break
        if valid:
            max_sum = max(max_sum, total)

def dfs(x, y, depth, total):
    global max_sum, n, m, grid, visited
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if depth == 4:
        max_sum = max(max_sum, total)
        return
    
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        if 0 <= next_x < n and 0 <= next_y < m:
            if not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                dfs(next_x, next_y, depth + 1, total + grid[next_x][next_y])
                visited[next_x][next_y] = False

def solve_max_sum(n, m, grid):
    global max_sum, visited
    max_sum = 0
    visited = [[False] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            visited[x][y] = True
            dfs(x, y, 1, grid[x][y])
            visited[x][y] = False
            check_t_shape(x, y)
    
    return max_sum

def main():
    global n, m, grid, t_shape
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    t_shape = [
        [(0 ,-1), (-1, 0), (0, 1)],
        [(0, -1), (1, 0), (0, 1)],
        [(0, -1), (-1, 0), (1, 0)],
        [(0, 1), (-1, 0), (1, 0)]
    ]

    print(solve_max_sum(n, m, grid))

if __name__ == '__main__':
    main()