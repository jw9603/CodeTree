
dir = [(0,1),(-1,0),(0,-1),(1,0)]  # 각각 동북서남

N = int(input())
graph = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())  # 각각 좌표, 시작방향, 세대 수
    graph[x][y] += 1
    todo = [d]
    x = x+dir[d][0]
    y = y+dir[d][1]
    graph[x][y] += 1
    todo = [(d+1)%4]  # 이쪽의 turn까지 0세대 처리

    for _ in range(g):  # 여기는 1세대부터 처리
        for i in range(len(todo)):
            x = x+dir[todo[i]][0]
            y = y+dir[todo[i]][1]
            graph[x][y] += 1
        todo = todo[::-1]+todo
        for i in range(len(todo)//2):
            todo[i] += 1
            todo[i] %= 4
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i+1][j] and graph[i][j+1] and graph[i+1][j+1]:
            cnt += 1
print(cnt)