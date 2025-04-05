from collections import deque
def bfs(x, y, grid, robot_level, n):
    queue = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    min_dist = float('inf')
    mon_list = []

    while queue:
        cur_x, cur_y, cur_d = queue.popleft()

        if 0 < grid[cur_x][cur_y] < robot_level:

            if cur_d < min_dist:
                min_dist = cur_d
                mon_list = [(cur_x, cur_y, cur_d)]
            elif cur_d == min_dist:
                mon_list.append((cur_x, cur_y, cur_d))

        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy

            if 0 <= next_x < n and 0 <= next_y < n:
                if grid[next_x][next_y] <= robot_level and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_d + 1))
    
    if mon_list:
        mon_list.sort()
        return mon_list[0]
    return None

def main():
    n = int(input().strip())
    grid = [list(map(int, input().split())) for _ in range(n)]

    robot_level = 2
    mon_killed = 0
    time = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 9:
                robot_x, robot_y = i, j
                grid[i][j] = 0
    
    while True:
        
        result = bfs(robot_x, robot_y, grid, robot_level, n)

        if not result:
            break
        
        robot_x, robot_y, move_time = result
        time += move_time

        mon_killed += 1
        grid[robot_x][robot_y] = 0

        if mon_killed == robot_level:
            robot_level += 1
            mon_killed = 0

    print(time)

if __name__ == '__main__':
    main()