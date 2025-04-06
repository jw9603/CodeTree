from collections import deque
def remove_adjacent(board, N, M):
    removed = False
    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_removed = set()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or visited[i][j]:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            same = [(i, j)]
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, (y + dy) % M
                    if 0 <= nx < N and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        same.append((nx, ny))
            
            if len(same) > 1:
                removed = True
                for x, y in same:
                    to_removed.add((x, y))
    
    for x, y in to_removed:
        board[x][y] = 0
    
    return removed

def adjust_numbers(board, N, M):
    '''
    없는 경우에는 원판에 적힌 수의 평균을 구하고, 
    평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
    '''
    total = 0
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                total += board[i][j]
                cnt += 1
    if not cnt:
        return
 
    avg = total / cnt
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0: # 0은 원판에 적힌 수가 아님
                continue
            if board[i][j] > avg:
                board[i][j] -= 1
            elif board[i][j] < avg:
                board[i][j] += 1

def rotate(board, x, d, k, N):
    for i in range(x - 1, N, x):
        if d == 0: # 시계
            board[i].rotate(k)
        else:
            board[i].rotate(-k)

def main():
    N, M, T = map(int, input().split())
    board = [deque(map(int, input().split())) for _ in range(N)]
    operations = [tuple(map(int, input().split())) for _ in range(T)]

    for x, d, k in operations:
        rotate(board, x, d, k, N)
        if not remove_adjacent(board, N, M): # 제거할 게 없을 때 아래 실행
            adjust_numbers(board, N, M)
    
    print(sum(map(sum, board)))

if __name__ == '__main__':
    main()