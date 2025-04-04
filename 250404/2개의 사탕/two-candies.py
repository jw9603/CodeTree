from collections import deque
def move(x, y, dx, dy, board):
    cnt = 0

    while board[x][y] != '#' and board[x][y] != 'O' and board[x + dx][y + dy] != '#':
        x += dx
        y += dy
        cnt += 1
    
    return x, y, cnt

def bfs(board, rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by, 0)])
    visited = set()
    visited.add((rx, ry, bx, by))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        rx, ry, bx, by, cur_t = queue.popleft()

        if cur_t >= 10:
            continue
        
        for dx, dy in directions:
            next_rx, next_ry, r_cnt = move(rx, ry, dx, dy, board)
            next_bx, next_by, b_cnt = move(bx, by, dx, dy, board)

            if board[next_bx][next_by] == 'O':
                continue
            
            if board[next_rx][next_ry] == 'O':
                return cur_t + 1
            
            if (next_rx, next_ry) == (next_bx, next_by):
                if r_cnt < b_cnt:
                    next_bx -= dx
                    next_by -= dy
                else:
                    next_rx -= dx
                    next_ry -= dy
            
            if (next_rx, next_ry, next_bx, next_by) not in visited:
                visited.add((next_rx, next_ry, next_bx, next_by))
                queue.append((next_rx, next_ry, next_bx, next_by, cur_t + 1))
    
    return -1

def sol(N, M, board):
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    
    return bfs(board, rx, ry, bx, by)

def main():
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    print(sol(N, M, board))

if __name__ == '__main__':
    main()