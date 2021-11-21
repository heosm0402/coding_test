import sys

# i, j = map(int, sys.stdin.readline().rstrip().split())
i, j = 192, 162

def GCD(i, j):
    max_num = max(i, j)
    min_num = min(i, j)

    if max_num % min_num == 0:
        return min_num
    else:
        return GCD(min_num, max_num % min_num)

result = GCD(i, j)
print(result)

