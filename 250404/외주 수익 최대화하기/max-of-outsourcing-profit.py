def dfs(day, curr_profit):
    global n, max_profit, schedules

    if day > n:
        max_profit = max(max_profit, curr_profit)
        return
    
    dfs(day + 1, curr_profit)

    if day + schedules[day][0] - 1 <= n:
        dfs(day + schedules[day][0], curr_profit + schedules[day][1])

def main():
    global n, max_profit, schedules
    n = int(input().strip())
    schedules = [None] + [tuple(map(int, input().split())) for _ in range(n)]

    max_profit = 0

    dfs(1, 0)

    print(max_profit)

if __name__ == '__main__':
    main()