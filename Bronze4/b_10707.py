# https://www.acmicpc.net/problem/10707
import sys


if __name__ == "__main__":
    com_1_per_liter = int(sys.stdin.readline().rstrip())

    com_2_basic_cost = int(sys.stdin.readline().rstrip())
    com_2_basic_limit = int(sys.stdin.readline().rstrip())
    com_2_per_liter = int(sys.stdin.readline().rstrip())

    used_liter = int(sys.stdin.readline().rstrip())

    com_1 = used_liter * com_1_per_liter

    if used_liter >= com_2_basic_limit:
        com_2 = com_2_basic_cost + ((used_liter - com_2_basic_limit) * com_2_per_liter)
        print(min(com_1, com_2))
    else:
        com_2 = com_2_basic_cost
        print(min(com_1, com_2))
