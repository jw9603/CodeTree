from collections import deque
def rotate(table, direction):
    table.rotate(direction)

def process_table(tables, tab_idx, direction):
    directions = [0] * 4
    directions[tab_idx] = direction

    for i in range(tab_idx, 0, -1):
        if tables[i][6] != tables[i - 1][2]:
            directions[i - 1] = -directions[i]
        else:
            break
    
    for i in range(tab_idx, 3):
        if tables[i][2] != tables[i + 1][6]:
            directions[i + 1] = -directions[i]
        else:
            break
    
    for i in range(4):
        if directions[i] != 0:
            rotate(tables[i], directions[i])

def calculate_tables(tables):
    scores_table = [1, 2, 4, 8]
    scores = 0

    for i in range(4):
        if tables[i][0] == 1:
            scores += scores_table[i]
    
    return scores

def main():
    tables = [deque(map(int, input().strip())) for _ in range(4)]
    k = int(input().strip())
    for _ in range(k):
        tab_num, direction = map(int, input().split())
        process_table(tables, tab_num - 1, direction)
    
    print(calculate_tables(tables))

if __name__ == '__main__':
    main()