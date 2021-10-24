# https://www.acmicpc.net/problem/3003
import sys


if __name__ == "__main__":
    present_set = list(map(int, sys.stdin.readline().rstrip().split()))
    correct_set = [1, 1, 2, 2, 2, 8]
    print(*[correct_set[idx] - present_set[idx] for idx in range(len(correct_set))])
