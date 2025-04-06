def move_horse(board, horses, board_map, idx, n):
    global dx, dy, reversed_dir

    x, y, d = horses[idx]

    nx, ny = x + dx[d], y + dy[d]

    pos = board_map[x][y].index(idx)
    moving_stack = board_map[x][y][pos:]
    board_map[x][y] = board_map[x][y][:pos]

    # 파란색
    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:

        d = reversed_dir[d]
        horses[idx][2] = d
        nx, ny = x + dx[d], y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            board_map[x][y].extend(moving_stack)
            return False
    
    # 하얀색, 빨간색 이동
    if board[nx][ny] == 0:
        board_map[nx][ny].extend(moving_stack)
    elif board[nx][ny] == 1:
        board_map[nx][ny].extend(reversed(moving_stack))

    for horse in moving_stack:
        horses[horse][0] = nx
        horses[horse][1] = ny
    
    if len(board_map[nx][ny]) >= 4:
        return True
    
    return False

def simulate(n, k, board, horses):
    board_map = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(k):
        x, y, _ = horses[i]
        board_map[x][y].append(i)

    for turn in range(1, 1001):
        for i in range(k):
            if move_horse(board, horses, board_map, i, n):
                return turn
    
    return -1

def main():
    global dx, dy, reversed_dir
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    horses = []
    for _ in range(k):
        x, y, d = map(int, input().split())
        horses.append([x - 1, y - 1, d])
    
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    reversed_dir = [0, 2, 1, 4, 3]

    print(simulate(n, k, board, horses))

if __name__ == '__main__':
    main()