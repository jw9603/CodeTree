def change_board(board, x, y, directions):
    tmp_board = [row[:] for row in board]

    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy

        while 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
            if tmp_board[next_x][next_y] == 6:
                break
            
            if tmp_board[next_x][next_y] == 0:
                tmp_board[next_x][next_y] = '#'
            
            next_x += dx
            next_y += dy
    
    return tmp_board

def dfs(depth, board, chess, chess_modes):
    global min_space

    if depth == len(chess):
        cnt = sum(row.count(0) for row in board)
        min_space = min(min_space, cnt)
        return
    
    x, y, chess_type = chess[depth]

    for directions in chess_modes[chess_type]:
        new_board = change_board(board, x, y, directions)
        dfs(depth + 1, new_board, chess, chess_modes)

def main():
    global min_space
    n, m = map(int, input().split())

    board, chess = [], []
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(m):
            if 1 <= row[j] <= 5:
                chess.append((i, j, row[j]))
    
    min_space = float('inf')

    chess_modes = {
        1 : [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
        2 : [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
        3 : [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        4 : [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
        5 : [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
    }

    dfs(0, board, chess, chess_modes)

    print(min_space)

if __name__ == '__main__':
    main()