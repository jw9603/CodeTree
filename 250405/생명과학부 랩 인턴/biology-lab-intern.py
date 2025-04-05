from collections import defaultdict
def find_dust(n, m,  dust):
    directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    total = 0

    grid = defaultdict(list)
    for x, y, s, d, b in dust:
        # s: 속력, d: 이동 방향, b: 곰팡이 크기
        grid[(x - 1, y - 1)] = [s, d, b]
    
    for intern_col in range(m):
        target = None
        
        for row in range(n):
            if (row, intern_col) in grid:
                target = (row, intern_col)
                break
        if target:
            total += grid[target][2]
            del grid[target]

        # 2. 곰팡이 이동
        new_grid = defaultdict(list)
        for (x, y), (s, d, b) in grid.items():
            cur_x, cur_y, cur_d = x, y, d

            speed = s

            if cur_d in [1, 2]:
                speed %= (2 * (n - 1))
            else:
                speed %= (2 * (m - 1))
            
            for _ in range(speed):
                nx = cur_x + directions[cur_d][0]
                ny = cur_y + directions[cur_d][1]

                if not (0 <= nx < n and 0 <= ny < m):
                    if cur_d == 1:
                        cur_d = 2
                    elif cur_d == 2:
                        cur_d = 1
                    elif cur_d == 3:
                        cur_d = 4
                    elif cur_d == 4:
                        cur_d = 3
                    
                    nx = cur_x + directions[cur_d][0]
                    ny = cur_y + directions[cur_d][1]
                
                cur_x, cur_y = nx, ny

            if new_grid[(cur_x, cur_y)]:
                if new_grid[(cur_x, cur_y)][2] < b:
                    new_grid[(cur_x, cur_y)] = (s, cur_d, b)
            else:
                new_grid[(cur_x, cur_y)] = (s, cur_d, b)

        grid = new_grid
    
    return total

def main():
    n, m, k = map(int, input().split())

    dust = [tuple(map(int, input().split())) for _ in range(k)]

    print(find_dust(n, m, dust))

if __name__ == '__main__':
    main()