def main():
    N = int(input().strip())

    visited = [[False] * 101 for _ in range(101)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for _ in range(N):
        x, y, d, g = map(int, input().split())

        directions = [d]
        for _ in range(g):
            for i in reversed(range(len(directions))):
                directions.append((directions[i] + 1) % 4)
        
        points = [(x, y)]
        for direction in directions:
            last_x, last_y = points[-1]
            nx = last_x + dx[direction]
            ny = last_y + dy[direction]
            points.append((nx, ny))
        
        for px, py in points:
            if 0 <= px <= 100 and 0 <= py <= 100:
                visited[py][px] = True
    
    cnt = 0
    for i in range(100):
        for j in range(100):
            if visited[i][j] and visited[i + 1][j] and visited[i][j + 1] and visited[i + 1][j + 1]:
                cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    main()     