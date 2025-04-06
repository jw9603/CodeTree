def mark_boundary(x, y, d1, d2, N):
    boundary = [[0] * N for _ in range(N)]

    # 5번 선거구 경계선 표시
    for i in range(d1 + 1):
        boundary[x + i][y - i] = 5
        boundary[x + d2 + i][y + d2 - i] = 5
    
    for i in range(d2 + 1):
        boundary[x + i][y + i] = 5
        boundary[x + d1 + i][y - d1 + i] = 5
    
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
            # 5번 선거구 (경계 포함 및 내부)
            if boundary[r][c] == 5:
                sections[4] += A[r][c]
            # 1번 선거구
            elif 0 <= r < x + d1 and 0 <= c <= y:
                sections[0] += A[r][c]
            # 2번 선거구
            elif 0 <= r <= x + d2 and y < c < N:
                sections[1] += A[r][c]
            # 3번 선거구
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                sections[2] += A[r][c]
            # 4번 선거구
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                sections[3] += A[r][c]
            # 🔥 위에 해당 안되는 셀이 있을 수 있음. 방어 코드 추가 (디버깅용)
            else:
                sections[4] += A[r][c]  # 혹은 5번 선거구에 포함
    return max(sections) - min(sections)


def calculate_population_diff(N, A):
    min_diff = float('inf')

    for x in range(N):
        for y in range(N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if x + d1 + d2 < N and 0 <= y - d1 and y + d2 < N:
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