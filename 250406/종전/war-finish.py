def mark_boundary(x, y, d1, d2, N):
    boundary = [[0] * N for _ in range(N)]

    # 5번 경계선 설정
    for i in range(d1 + 1):
        boundary[x + i][y - i] = 5
        boundary[x + d2 + i][y + d2 - i] = 5
    
    for i in range(d2 + 1):
        boundary[x + i][y + i] = 5
        boundary[x + d1 + i][y - d1 + i] = 5

    # 경계 내부를 5로 채우기
    for r in range(x + 1, x + d1 + d2):
        fill = False
        for c in range(N):
            if boundary[r][c] == 5:
                fill = not fill
            elif fill:
                boundary[r][c] = 5

    return boundary


def divide_sections(x, y, d1, d2, boundary, A, N):
    sections = [0] * 5
    for r in range(N):
        for c in range(N):
            if boundary[r][c] == 5:
                sections[4] += A[r][c]
            elif 0 <= r < x + d1 and 0 <= c <= y:
                sections[0] += A[r][c]
            elif 0 <= r <= x + d2 and y < c < N:
                sections[1] += A[r][c]
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                sections[2] += A[r][c]
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                sections[3] += A[r][c]
            else:
                sections[4] += A[r][c]  # 경계로 둘러싸인 남은 곳
    return max(sections) - min(sections)


def calculate_population_diff(N, A):
    min_diff = float('inf')

    for x in range(N):
        for y in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if x + d1 + d2 >= N:
                        continue
                    if y - d1 < 0 or y + d2 >= N:
                        continue

                    boundary = mark_boundary(x, y, d1, d2, N)
                    diff = divide_sections(x, y, d1, d2, boundary, A, N)
                    min_diff = min(min_diff, diff)
    
    return min_diff


def main():
    N = int(input().strip())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(calculate_population_diff(N, A))


if __name__ == '__main__':
    main()
