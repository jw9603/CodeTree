dir = [(0,1),(-1,0),(0,-1),(1,0)]  # 각각 동북서남

N = int(input())
graph = [[0]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    todo = [d]
    
    if 0 <= x < 101 and 0 <= y < 101:
        graph[x][y] = 1

    x += dir[d][0]
    y += dir[d][1]

    if 0 <= x < 101 and 0 <= y < 101:
        graph[x][y] = 1

    for _ in range(g):
        temp = []
        for i in reversed(todo):
            temp.append((i + 1) % 4)
        todo += temp

        for i in temp:
            x += dir[i][0]
            y += dir[i][1]
            if 0 <= x < 101 and 0 <= y < 101:
                graph[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            cnt += 1
print(cnt)
