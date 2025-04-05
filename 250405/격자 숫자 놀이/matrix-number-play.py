
from collections import Counter
def operate_r(grid):
    max_len = 0
    new_grid = []

    for row in grid:
        counter = sorted(Counter([num for num in row if num != 0]).items(), key=lambda x: (x[1], x[0]))
        sorted_row = []
        for num, cnt in counter:
            sorted_row.extend([num, cnt])
        
        new_grid.append(sorted_row)
        max_len = max(max_len, len(sorted_row))
    
    for row in new_grid:
        while len(row) < max_len:
            row.append(0)
        row[:] = row[:100]
    
    return new_grid

def operate_c(grid):
    transposed = [list(row) for row in zip(*grid)]
    operated = operate_r(transposed)

    return [list(row) for row in zip(*operated)]

def sol(r, c, k, grid):

    for time in range(101):
        if 0 <= r - 1 < len(grid) and 0 <= c - 1 < len(grid[0]):
            if grid[r - 1][c- 1] == k:
                print(time)
                return
        
        if len(grid) >= len(grid[0]):
            grid = operate_r(grid)
        else:
            grid = operate_c(grid)
            
    print(-1)

def main():
    r, c, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(3)]

    sol(r, c, k, grid)

if __name__ == '__main__':
    main()