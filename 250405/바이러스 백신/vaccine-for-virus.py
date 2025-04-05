from collections import deque
def bfs(selected, N, grid):
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x, y in selected:
        visited[x][y] = True
        queue.append((x, y, 0))
    
    virus_cnt = sum(row.count(0) for row in grid)
    
    time = 0
    cured = 0

    while queue:
        cur_x, cur_y, cur_t = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y] and grid[next_x][next_y] != 1:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_t + 1))

                    if grid[next_x][next_y] == 0:
                        cured += 1
                        time = max(time, cur_t + 1)
    
    return time if cured == virus_cnt else float('inf')
                    
def find_min_time(N, M, grid):
    hosp_spaces = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 2:
                hosp_spaces.append((i, j))
    
    min_time = float('inf')

    def dfs(start, selected):
        nonlocal min_time
        if len(selected) == M:
            min_time = min(min_time, bfs(selected, N, grid))
            return

        for i in range(start, len(hosp_spaces)):
            selected.append(hosp_spaces[i])
            dfs(i + 1, selected)
            selected.pop()
    
    dfs(0, [])

    return min_time if min_time != float('inf') else -1

def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(find_min_time(N, M, grid))

if __name__ == '__main__':
    main()