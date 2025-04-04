def can_place(ladder, i, j, n):

    if ladder[i][j]:
        return False

    if j > 0 and ladder[i][j - 1]:
        return False
    
    if j < n - 2 and ladder[i][j + 1]:
        return False
    
    return True

def simulate(ladder, n, h):

    for start in range(n):
        k = start
        
        for row in range(h):
            if k < n - 1 and ladder[row][k]:
                k += 1
            elif k > 0 and ladder[row][k - 1]:
                k -= 1

        if k != start:
            return False
    
    return True

def dfs(depth, ladder, n, h, row, col):
    global result

    if depth >= result:
        return

    if simulate(ladder, n, h):
        result = depth
        return

    if depth == 3:
        return
    
    for i in range(row, h):
        sj = col if row == i else 0
        for j in range(sj, n - 1):
            if can_place(ladder, i, j, n):
                ladder[i][j] = True
                dfs(depth + 1, ladder, n, h, i, j + 2)
                ladder[i][j] = False

def sol(n, m, h):
    global result
    ladder = [[False] * (n - 1) for _ in range(h)]
    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a - 1][b - 1] = True
    
    result = 4
    dfs(0, ladder, n, h, 0, 0)

    return result if result <= 3 else -1

def main():
    n, m, h = map(int, input().split())

    print(sol(n, m, h))

if __name__ == '__main__':
    main()