from collections import deque
def bfs(n, m, grid, fire_spaces):
    queue = deque(fire_spaces)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    tmp_lab = [row[:] for row in grid]

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < n and 0 <= next_y < m:
                if tmp_lab[next_x][next_y] == 0:
                    tmp_lab[next_x][next_y] = 2
                    queue.append((next_x, next_y))
    return sum(row.count(0) for row in tmp_lab)

def count_safe_areas(depth, start, n, m, grid, empty_spaces, fire_spaces):
    global max_safe_areas

    if depth == 3:
        max_safe_areas = max(max_safe_areas, bfs(n, m, grid, fire_spaces))
        return

    for i in range(start, len(empty_spaces)):
        x, y = empty_spaces[i]
        grid[x][y] = 1
        count_safe_areas(depth + 1, i + 1, n, m, grid, empty_spaces, fire_spaces)
        grid[x][y] = 0

def main():
    global max_safe_areas
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    empty_spaces = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0]
    fire_spaces = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == 2]

    max_safe_areas = 0

    count_safe_areas(0, 0, n, m, grid, empty_spaces, fire_spaces)

    print(max_safe_areas)

if __name__ == '__main__':
    main()