def dfs(index, current_val, plus, minus, mul):
    global n, nums, max_val, min_val

    # 1. base case
    if index == n:
        max_val = max(max_val, current_val)
        min_val = min(min_val, current_val)
        return

    if plus > 0:
        dfs(index + 1, current_val + nums[index], plus - 1, minus, mul)
    if minus > 0:
        dfs(index + 1, current_val - nums[index], plus, minus - 1, mul)
    if mul > 0:
        dfs(index + 1, current_val * nums[index], plus, minus, mul - 1)

def main():
    global n, nums, max_val, min_val
    n = int(input().strip())
    nums = list(map(int, input().split()))
    operators_cnt = list(map(int, input().split())) # +, -, x
    max_val, min_val = -float('inf'), float('inf')

    dfs(1, nums[0], *operators_cnt)

    print(min_val, max_val)

if __name__ == '__main__':
    main()