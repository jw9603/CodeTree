from collections import deque
def bfs(x, y, grid, visited, n, L, R):
    queue = deque([(x, y)])
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0 ,-1), (0, 1)]

    union = [(x, y)]
    total = grid[x][y]

    while queue:
        cur_x, cur_y = queue.popleft()

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
                if L <= abs(grid[next_x][next_y] - grid[cur_x][cur_y]) <= R:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y))
                    union.append((next_x, next_y))
                    total += grid[next_x][next_y]
    
    if len(union) > 1:
        new_total = total // len(union)
        for ux, uy in union:
            grid[ux][uy] = new_total
        return True
    
    return False

def sol(n, L, R, grid):
    cnt = 0

    while True:
        visited = [[False] * n for _ in range(n)]
        move = False

        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(i, j, grid, visited, n, L, R):
                        move = True
        
        if not move:
            break

        cnt += 1
    
    return cnt

def main():
    n, L, R = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(sol(n, L, R, grid))

if __name__ == '__main__':
    main()