def dfs(start, team_morning):
    global n, P, min_diff

    if len(team_morning) == n // 2:
        team_night = [i for i in range(n) if i not in set(team_morning)]
        ability_morning = sum(P[i][j] + P[j][i] for i in team_morning for j in team_morning if i < j)
        ability_night = sum(P[i][j] + P[j][i] for i in team_night for j in team_night if i < j)

        min_diff = min(min_diff, abs(ability_morning - ability_night))
        return

    for i in range(start, n):
        team_morning.append(i)
        dfs(i + 1, team_morning)
        team_morning.pop()

def main():
    global n, P, min_diff
    n = int(input().strip())
    P = [list(map(int, input().split())) for _ in range(n)]

    min_diff = float('inf')
    dfs(0, [])
    print(min_diff)

if __name__ == '__main__':
    main()