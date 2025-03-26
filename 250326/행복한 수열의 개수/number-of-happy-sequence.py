def is_happy_seq(seq, m):
    cnt = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            cnt += 1
            if cnt >= m:
                return True
        else:
            cnt = 1
    return False

def happy_seq_cnt(n, m, grid):
    if m == 1:
        return n * 2

    cnt = 0

    for row in grid:
        if is_happy_seq(row, m):
            cnt += 1
    
    for col in zip(*grid):
        if is_happy_seq(col, m):
            cnt += 1
    
    return cnt

def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    print(happy_seq_cnt(n, m, grid))

if __name__ == '__main__':
    main()