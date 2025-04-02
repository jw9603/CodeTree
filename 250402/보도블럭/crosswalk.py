def can_pass(line, L):
    n = len(line)
    visited = [False] * n

    for i in range(n - 1):
        if line[i] == line[i + 1]:
            continue
        
        elif line[i] + 1 == line[i + 1]:
            for j in range(i, i - L, -1):
                if j < 0 or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True
        
        elif line[i] - 1 == line[i + 1]:
            for j in range(i + 1, i + 1 + L):
                if j >= n or line[j] != line[i + 1] or visited[j]:
                    return False
                visited[j] = True
        
        else:
            return False
    return True

def cnt_pass(grid, L):
    cnt = 0

    for row in grid:
        if can_pass(row, L):
            cnt += 1
    
    for col in zip(*grid):
        if can_pass(col, L):
            cnt += 1
    
    return cnt

def main():
    n, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(cnt_pass(grid, L))

if __name__ == '__main__':
    main()