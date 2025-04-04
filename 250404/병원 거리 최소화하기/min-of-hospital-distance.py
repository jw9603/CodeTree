def calculated_hospital_distance(people, selected):
    total_distance = 0

    for px, py in people:
        cur_distance = float('inf')
        for hx, hy in selected:
            cur_distance = min(cur_distance, abs(px - hx) + abs(py - hy))
        total_distance += cur_distance
    
    return total_distance

def dfs(start, selected, people, hospitals, m):
    global min_distance

    if len(selected) == m:
        hosp_distance = calculated_hospital_distance(people, selected)
        min_distance = min(min_distance, hosp_distance)
        return

    for i in range(start, len(hospitals)):
        selected.append(hospitals[i])
        dfs(i + 1, selected, people, hospitals, m)
        selected.pop()

def sol(n, m, city):
    global min_distance
    min_distance = float('inf')

    people, hospitals = [], []

    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                people.append((i, j))
            elif city[i][j] == 2:
                hospitals.append((i, j))
    
    dfs(0, [], people, hospitals, m)

    return min_distance

def main():
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]

    print(sol(n, m, city))

if __name__ == '__main__':
    main()