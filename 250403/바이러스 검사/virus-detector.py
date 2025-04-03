def solution(clients, a, b):
    cnt = 0

    for client in clients:
        cnt += 1
        client -= a

        if client > 0:
            cnt += client // b
            if client % b != 0:
                cnt += 1
    return cnt

def main():
    n = int(input().strip())
    clients = list(map(int, input().split()))
    a, b = map(int, input().split())

    print(solution(clients, a, b))

if __name__ == '__main__':
    main()