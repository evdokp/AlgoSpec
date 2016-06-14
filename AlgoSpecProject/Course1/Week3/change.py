# Uses python3
import sys

def get_change(n):
    m = n
    coins = [1,5,10]
    min_nums = dict()
    min_nums[0] = 0
    for m in range(1, m + 1):
        min_nums[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                if min_nums[m - coins[i]] + 1 < min_nums[m]:
                    min_nums[m] = min_nums[m - coins[i]] + 1
    return min_nums[m]

if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
