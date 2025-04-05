def steps(n, k, A, virus):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    nutrients = [[5] * n for _ in range(n)]

    for _ in range(k):

        # 1. 각각의 바이러스는 본인이 속한 1 x 1 크기의 칸에 있는 양분을 섭취
        # 본인의 나이만큼 양분을 섭취하며, 같은 칸에 여러 개의 바이러스가 있을 때에는 나이가 어린 바이러스부터 양분을 섭취
        dead = [[[] for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if not virus[i][j]:
                    continue

                virus[i][j].sort()
                survived = []

                for age in virus[i][j]:
                    if nutrients[i][j] >= age:
                        nutrients[i][j] -= age
                        survived.append(age + 1)
                    else:
                        dead[i][j].append(age)

                virus[i][j] = survived
        
        # 2. 모든 바이러스가 섭취를 끝낸 후 죽은 바이러스가 양분으로 변한다.
        # 죽은 바이러스마다 나이를 2로 나눈 값이 바이러스가 있던 칸에 양분으로 추가된다.
        for i in range(n):
            for j in range(n):
                for dead_age in dead[i][j]:
                    nutrients[i][j] += dead_age // 2
        
        # 3. 번식을 진행
        # 번식은 5의 배수의 나이를 가진 바이러스에게만 진행되며, 인접한 8개의 칸에 나이가 1인 바이러스가 생김
        for i in range(n):
            for j in range(n):
                for age in virus[i][j]:
                    if age % 5 == 0:
                        for dx, dy in directions:
                            next_i, next_j = i + dx, j + dy
                            if 0 <= next_i < n and 0 <= next_j < n:
                                virus[next_i][next_j].insert(0, 1)
        
        # 주어진 양분의 양에 따라 칸에 양분이 추가된다.
        for i in range(n):
            for j in range(n):
                nutrients[i][j] += A[i][j]
        
    result = 0
    for i in range(n):
        for j in range(n):
            result += len(virus[i][j])
    
    return result

def main():
    n, m, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]

    virus = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        r, c, z = map(int, input().split())
        virus[r - 1][c - 1].append(z)
    
    print(steps(n, k, A, virus))

if __name__ == '__main__':
    main()